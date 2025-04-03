import os
import hashlib
import pandas as pd
import random  # Pour les variations aléatoires
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
def mask_value(value, column_type):
    value = str(value)
    if column_type == 'name':
        parts = value.split()
        if len(parts) > 1:
            first_name_initial = parts[0][0]  # Première lettre du prénom
            last_name_initial = parts[1][0]   # Première lettre du nom
            masked_first_name = first_name_initial + "*" * (len(parts[0]) - 1)
            masked_last_name = last_name_initial + "*" * (len(parts[1]) - 1)
            masked_name = f"{masked_first_name} {masked_last_name}"
            return masked_name
        return value
    elif column_type == 'email':
        if '@' in value:
            local_part, domain = value.split('@', 1)
            masked_local = local_part[0] + "*" * (len(local_part) - 1)
            return f"{masked_local}@{domain}"
        return value
    elif column_type == 'telephone':
        return value[:2] + "*" * (len(value) - 4) + value[-2:]
    return value

# Fonction pour généraliser les dates (en ne gardant que l'année)
def generalize_date(value):
    try:
        # Convertir la valeur en date et ne garder que l'année
        return pd.to_datetime(value).year
    except Exception as e:
        # Si ce n'est pas une date valide, renvoyer la valeur originale
        return value

# Fonction pour retirer le numéro de rue dans une adresse
def remove_street_number(address):
    # Retirer tout avant la première virgule ou espace (hypothèse que l'adresse commence par un numéro de rue)
    return address.split(',')[-1].strip() if ',' in address else address.split(' ', 1)[-1]

# Appliquer une variation aléatoire de ±5% à une valeur numérique, en gardant le format d'origine
def apply_random_variation(value, variation_percentage):
    try:
        # Convertir la valeur en float (si possible)
        num_value = float(value)

        # Appliquer la variation de ±variation_percentage
        new_value = num_value * (1 + variation_percentage)

        # Vérifier si la valeur originale était un entier (c'est-à-dire pas de décimale)
        if num_value.is_integer():
            return int(new_value)  # Convertir en entier si l'original était un entier
        else:
            # Conserver le même nombre de décimales qu'à l'origine
            return round(new_value, len(str(value).split('.')[-1]))  # Conserver le nombre de décimales
    except ValueError:
        # Si la conversion échoue (valeur non numérique), retourner la valeur originale
        return value


# Vérifier si l'extension du fichier est autorisée
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/anonymize', methods=['POST'])
def anonymize():
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier trouvé'}), 400
    file = request.files['file']

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
    else:
        return jsonify({'error': 'Le fichier doit être au format CSV'}), 400

    df = pd.read_csv(file_path)

    # Obtenir les types de colonnes envoyés par le frontend
    column_types = {key.strip().replace('%0D%0A', ''): value for key, value in request.form.items()}

    print(column_types)

    # Supprimer la colonne de type 'id'
    for column in df.columns:
        column_type = column_types.get(f'{column}_type', None)
        if column_type == 'id':  # Si la colonne est de type 'id', on la supprime
            df.drop(column, axis=1, inplace=True)
            break  # On sort de la boucle après avoir supprimé la première colonne de type 'id'

    # Traitement pour la colonne adresse
    has_ville_column = 'ville' in column_types.values()

    if has_ville_column:
        # Si une colonne 'ville' existe, on supprime la colonne 'adresse'
        adresse_columns = [col for col in df.columns if column_types.get(f'{col}_type', '') == 'adresse']
        for col in adresse_columns:
            df.drop(col, axis=1, inplace=True)
    else:
        # Sinon, on modifie les valeurs dans la colonne 'adresse'
        adresse_columns = [col for col in df.columns if column_types.get(f'{col}_type', '') == 'adresse']
        for col in adresse_columns:
            df[col] = df[col].apply(remove_street_number)

    # Appliquer des masquages pour les autres colonnes en fonction de leur type
    variation_percentage = random.uniform(-0.05, 0.05)  # Variation aléatoire à appliquer à toutes les colonnes 'chiffre'
    for column in df.columns:
        column_type = column_types.get(f'{column}_type', None)

        if column_type:
            if column_type == 'name':
                # Appliquer un masquage pour les colonnes de type 'name'
                df[column] = df[column].apply(lambda x: mask_value(x, column_type))
            elif column_type == 'email':
                # Appliquer un masquage pour les colonnes de type 'email'
                df[column] = df[column].apply(lambda x: mask_value(x, column_type))
            elif column_type == 'telephone':
                # Appliquer un masquage pour les colonnes de type 'telephone'
                df[column] = df[column].apply(lambda x: mask_value(x, column_type))
            elif column_type == 'date_naissance':  # Généralisation des dates
                df[column] = df[column].apply(generalize_date)
            elif column_type == 'chiffre':  # Appliquer la variation pour les colonnes de type 'chiffre'
                df[column] = df[column].apply(lambda x: apply_random_variation(x, variation_percentage))

    output_path = os.path.join(app.config['UPLOAD_FOLDER'], f'anonymized_{filename}')
    df.to_csv(output_path, index=False)

    return send_file(output_path, as_attachment=True, download_name=f'anonymized_{filename}', mimetype='text/csv')

if __name__ == '__main__':
    app.run(debug=True)
