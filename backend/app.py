from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Active CORS pour toutes les routes
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Exemples de données, tu peux les remplacer par des données dynamiques
    data = {"message": "Ca marche!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
