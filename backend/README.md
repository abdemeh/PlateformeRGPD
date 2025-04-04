# Backend - PlateformeRGPD

Le backend de la PlateformeRGPD est une API développée avec Flask. Elle permet de gérer l'anonymisation des données sensibles contenues dans des fichiers CSV.

## Table des matières

- [Structure du Projet](#structure-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Fonctionnalités Principales](#fonctionnalités-principales)

## Structure du Projet

La structure du dossier backend est la suivante :

```
backend/
├── app.py             # Serveur Flask pour gérer l'anonymisation.
├── uploads/           # Dossier pour les fichiers téléchargés.
├── requirements.txt   # Liste des dépendances Python.
└── README.md          # Documentation du backend.
```

## Installation

1. Cloner le dépôt :

    ```bash
    git clone https://github.com/abdemeh/PlateformeRGPD.git
    cd PlateformeRGPD/backend
    ```

2. Installer les dépendances nécessaires :

    ```bash
    pip install flask flask-cors pandas
    ```

## Utilisation

1. Lancer le serveur Flask :

    ```bash
    python app.py
    ```

    Le backend est accessible à l'adresse suivante : [http://localhost:5000](http://localhost:5000).

2. Tester l'API :

    Utiliser des outils comme [Postman](https://www.postman.com/) ou l'extension **REST Client** de Visual Studio Code pour envoyer des requêtes aux endpoints de l'API.

## Fonctionnalités Principales

- 📂 **Gestion des fichiers CSV** : Téléchargement et traitement des fichiers.
- 🔐 **Anonymisation des données** : Application de différentes méthodes d'anonymisation, notamment :
  - Masquage
  - Pseudonymisation
  - Généralisation
  - Perturbation
  - Agrégation
- 🌐 **API REST** : Communication avec le frontend pour transmettre les fichiers et les résultats.
- ⚙️ **Extensibilité** : Ajout possible de nouvelles méthodes d'anonymisation.