# Backend - PlateformeRGPD

Le backend de la PlateformeRGPD est une API développée avec Flask, permettant de gérer l'anonymisation des données sensibles contenues dans des fichiers CSV.

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

1. **Cloner le dépôt :**

    ```bash
    git clone https://github.com/abdemeh/PlateformeRGPD.git
    cd PlateformeRGPD/backend
    ```

2. **Installer les dépendances :**

    Exécutez la commande suivante pour installer Flask et les autres dépendances nécessaires :

    ```bash
    pip install flask flask-cors pandas
    ```

## Utilisation

1. **Lancer le serveur Flask :**

    Depuis le dossier `backend`, démarrez le serveur avec la commande suivante :

    ```bash
    python app.py
    ```

    Le backend sera accessible à l'adresse [http://localhost:5000](http://localhost:5000).

2. **Tester l'API :**

    Vous pouvez utiliser des outils comme [Postman](https://www.postman.com/) ou l'extension **REST Client** de Visual Studio Code pour tester les endpoints de l'API.

## Fonctionnalités Principales

- 📂 **Gestion des fichiers CSV** : Téléchargement et traitement des fichiers.
- 🔐 **Anonymisation des données** : Application de différentes méthodes d'anonymisation, telles que :
  - Masquage
  - Pseudonymisation
  - Généralisation
  - Perturbation
  - Agrégation
- 🌐 **API REST** : Communication avec le frontend pour transmettre les fichiers et les résultats.
- ⚙️ **Extensibilité** : Possibilité d'ajouter de nouvelles méthodes d'anonymisation.
