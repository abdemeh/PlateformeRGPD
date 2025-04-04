import os
import pandas as pd
from flask import Flask, request, send_file, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
from anonymizers import anonymize_column

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


import time

@app.route('/anonymize', methods=['POST'])
def anonymize():
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier trouvé'}), 400

    file = request.files['file']
    if not allowed_file(file.filename):
        return jsonify({'error': 'Le fichier doit être au format CSV'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    df = pd.read_csv(file_path)
    original_df = df.copy()

    start = time.time()

    # Anonymisation dynamique
    applied_methods = {}
    for column in df.columns:
        method = request.form.get(f"{column}_method")
        generalization_data = request.form.get(f"{column}_generalization")

        if method:
            applied_methods[column] = method
            df = anonymize_column(df, column, method, generalization_data)

    end = time.time()
    processing_time = round(end - start, 3)

    # ⚖️ Calcul des métriques
    total_cols = len(df.columns)
    modified_cols = len(applied_methods)
    fidelity_score = round((total_cols - modified_cols) / total_cols * 100, 2)
    reidentification_risk = round(1 - (modified_cols / total_cols), 2)
    gdpr_compliance = "Oui" if modified_cols > 0 else "Non"

    # Sauvegarde du fichier anonymisé
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], f"anonymized_{filename}")
    df.to_csv(output_path, index=False)

    return jsonify({
        "processing_time": processing_time,
        "estimated_reidentification_risk": reidentification_risk,
        "data_fidelity_score": fidelity_score,
        "gdpr_compliance": gdpr_compliance,
        "download_url": f"/download/{os.path.basename(output_path)}"
    })

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name=filename, mimetype='text/csv')
    return jsonify({"error": "Fichier non trouvé"}), 404


if __name__ == '__main__':
    app.run(debug=True)