import os
import hashlib
import pandas as pd
import random
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    """Vérifie que le fichier est un fichier CSV valide."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def mask_value(value, column_type):
    """Masque une valeur en fonction de son type (nom, email, téléphone, etc...)."""
    value = str(value)
    if column_type == 'name':
        return value[0] + '*' * (len(value) - 1) if value else value
    elif column_type == 'email':
        if '@' in value:
            local, domain = value.split('@')
            return local[0] + '*' * (len(local) - 1) + '@' + domain
    elif column_type == 'telephone':
        return value[:2] + '*' * (len(value) - 4) + value[-2:]
    elif column_type == 'carte_bancaire':
        return "**** **** **** " + value[-4:]
    elif column_type in ['solde', 'revenu', 'salaire']:
        return '*' * (len(str(value)) - 2) + str(value)[-2:]
    return value

def pseudonymize(value):
    """Retourne une pseudonymisation SHA256 (16 premiers caractères)."""
    return hashlib.sha256(str(value).encode('utf-8')).hexdigest()[:16]

def apply_random_variation(value, variation_percentage=0.05):
    """Applique une variation aléatoire de ±5% à une valeur numérique."""
    try:
        val = float(value)
        return round(val * (1 + random.uniform(-variation_percentage, variation_percentage)), 2)
    except:
        return value

def generalize_generic_date(value):
    """Généralise une date en gardant seulement l'année."""
    try:
        dt = pd.to_datetime(value)
        return f"{dt.year}"
    except:
        return value

def generalize_date_interval(value, bin_size=5):
    """Généralise une date en intervalle d'années (ex: 1990-1995)."""
    try:
        dt = pd.to_datetime(value)
        year = dt.year
        lower = (year // bin_size) * bin_size
        upper = lower + bin_size
        return f"{lower}-{upper}"
    except:
        return value

def generalize_balance(value):
    """Généralise un solde en une fourchette aléatoire de ±15%."""
    try:
        num_value = int(float(value))
        lower_margin = random.uniform(0, 0.15) * num_value
        upper_margin = random.uniform(0, 0.15) * num_value
        lower = int(num_value - lower_margin)
        upper = int(num_value + upper_margin)
        return f"{lower}-{upper}"
    except:
        return value

def generalize_numeric_interval(value, bin_size=5):
    """Généralise une valeur numérique en tranche fixe (ex: 50-55)."""
    try:
        num_value = float(value)
        lower = (int(num_value) // bin_size) * bin_size
        upper = lower + bin_size
        return f"{lower}-{upper}"
    except:
        return value

def generalize_country(value):
    """Généralise un pays en continent (Europe, Asie, etc...) avec possibilité de rajouter de nouveau pays."""
    continent_map = {
        'france': 'Europe', 'germany': 'Europe', 'poland': 'Europe',
        'czech republic': 'Europe', 'italy': 'Europe', 'china': 'Asie',
        'hong kong': 'Asie', 'japan': 'Asie', 'india': 'Asie',
        'indonesia': 'Asie', 'usa': 'Amérique du Nord', 'canada': 'Amérique du Nord',
        'peru': 'Amérique du Sud', 'brazil': 'Amérique du Sud', 'argentina': 'Amérique du Sud',
        'niger': 'Afrique', 'nigeria': 'Afrique', 'kenya': 'Afrique'
    }
    return continent_map.get(value.strip().lower(), "Autre")

def generalize_value(value, column_type):
    """Applique la généralisation adaptée au type donné."""
    if column_type == 'date_naissance':
        return generalize_date_interval(value)
    elif column_type == 'date':
        return generalize_generic_date(value)
    elif column_type == 'age':
        try:
            age = int(value)
            return f"{(age // 10) * 10}-{(age // 10) * 10 + 9}"
        except:
            return value
    elif column_type in ['solde', 'revenu', 'salaire']:
        return generalize_balance(value)
    elif column_type == 'pays':
        return generalize_country(value)
    elif column_type == 'chiffre':
        return generalize_numeric_interval(value)
    return value

def aggregate_column(values):
    """Retourne la moyenne des valeurs numériques d'une colonne."""
    try:
        values = pd.to_numeric(values, errors='coerce')
        return round(values.mean(), 2)
    except:
        return values

def remove_street_number(address):
    """Supprime le numéro de rue d'une adresse (en gardant le nom de la rue)."""
    return address.split(',')[-1].strip() if ',' in address else address.split(' ', 1)[-1]

@app.route('/anonymize', methods=['POST'])
def anonymize():
    """Traite et anonymise le fichier CSV reçu selon les méthodes et types choisis."""
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier trouvé'}), 400

    file = request.files['file']
    if not allowed_file(file.filename):
        return jsonify({'error': 'Le fichier doit être un .csv'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    df = pd.read_csv(file_path)

    column_types = {}
    column_methods = {}
    for key, value in request.form.items():
        if key.endswith('_type'):
            column = key.replace('_type', '')
            column_types[column] = value
        elif key.endswith('_method'):
            column = key.replace('_method', '')
            column_methods[column] = value

    for column in df.columns:
        if column_types.get(column) == 'id':
            df.drop(column, axis=1, inplace=True)

    if 'ville' in column_types.values():
        for col in df.columns:
            if column_types.get(col) == 'adresse':
                df.drop(col, axis=1, inplace=True)
    else:
        for col in df.columns:
            if column_types.get(col) == 'adresse':
                df[col] = df[col].apply(remove_street_number)

    for column in df.columns:
        method = column_methods.get(column)
        col_type = column_types.get(column)

        if method == 'masking':
            df[column] = df[column].apply(lambda x: mask_value(x, col_type))
        elif method == 'pseudonymization':
            df[column] = df[column].apply(pseudonymize)
        elif method == 'perturbation':
            df[column] = df[column].apply(lambda x: apply_random_variation(x))
        elif method == 'generalization':
            df[column] = df[column].apply(lambda x: generalize_value(x, col_type))
        elif method == 'aggregation':
            aggregated_value = aggregate_column(df[column])
            df[column] = [aggregated_value] * len(df)

    output_path = os.path.join(app.config['UPLOAD_FOLDER'], f'anonymized_{filename}')
    df.to_csv(output_path, index=False)

    return send_file(output_path, as_attachment=True, download_name=f'anonymized_{filename}', mimetype='text/csv')


if __name__ == '__main__':
    app.run(debug=True)
