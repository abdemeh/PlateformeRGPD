import os
import hashlib
import pandas as pd
from flask import Flask, request, send_file, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)

# Appliquer CORS à toutes les routes pour permettre l'accès depuis d'autres origines
CORS(app, resources={r"/*": {"origins": "*"}})

# Dossier où les fichiers téléchargés seront enregistrés
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Fonction de pseudonymisation : création d'un hachage SHA256 de la valeur
def pseudonymize(value):
    value = str(value)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()[:16]  # Prendre les 16 premiers caractères du hachage

# Fonction de masquage
def mask_value(value, column_name):
    value = str(value)
    if column_name.lower() == 'name':
        # Séparer le prénom et le nom
        parts = value.split()
        if len(parts) > 1:
            first_name_initial = parts[0][0]  # Première lettre du prénom
            last_name_initial = parts[1][0]   # Première lettre du nom
            # Masquer le reste des caractères sauf les initiales
            masked_first_name = first_name_initial + "." + "*" * (len(parts[0]) - 1)
            masked_last_name = last_name_initial + "." + "*" * (len(parts[1]) - 1)
            # Afficher les initiales et remplacer le reste par des astérisques
            masked_name = f"{masked_first_name} {masked_last_name}"
            return masked_name
        return value  # Si le format est invalide (pas de prénom et nom)
    elif column_name.lower() == 'email':
        if '@' in value:
            local_part, domain = value.split('@', 1)
            return f"{local_part[0]}***@{domain}"
        return value
    elif column_name.lower() == 'phone':
        return value[:4] + "****"
    return value

# Vérifier si l'extension du fichier est autorisée
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/anonymize', methods=['POST'])
def anonymize():
    # Vérification de la présence du fichier
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier trouvé'}), 400
    file = request.files['file']

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
    else:
        return jsonify({'error': 'Le fichier doit être au format CSV'}), 400

    # Lecture du fichier CSV avec pandas
    df = pd.read_csv(file_path)

    # Supprimer la colonne "id"
    if 'id' in df.columns:
        df.drop('id', axis=1, inplace=True)

    # Appliquer le masquage pour certaines colonnes spécifiques
    for column in df.columns:
        if column.lower() in ['name', 'email', 'phone']:
            df[column] = df[column].apply(lambda x: mask_value(x, column))

    # Enregistrer le fichier CSV anonymisé sans les colonnes identifiantes
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], f'anonymized_{filename}')
    df.to_csv(output_path, index=False)

    # Retourner le fichier anonymisé
    return send_file(output_path, as_attachment=True, download_name=f'anonymized_{filename}', mimetype='text/csv')

if __name__ == '__main__':
    app.run(debug=True)
