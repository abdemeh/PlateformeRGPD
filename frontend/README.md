# Frontend - PlateformeRGPD

Le frontend de la PlateformeRGPD est une application développée avec React et Vite. Il offre une interface utilisateur intuitive pour l'anonymisation des données sensibles contenues dans des fichiers CSV.

## Table des matières

- [Structure du Projet](#structure-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Fonctionnalités Principales](#fonctionnalités-principales)

## Structure du Projet

La structure du dossier frontend est la suivante :

```
frontend/
├── src/               # Code source React.
│   ├── App.jsx        # Composant principal de l'application.
│   ├── AnonymizationPage.jsx # Page principale pour l'anonymisation.
│   └── index.css      # Styles CSS globaux.
├── vite.config.js     # Configuration de Vite.
├── package.json       # Dépendances et scripts npm.
└── README.md          # Documentation du frontend.
```

## Installation

1. **Cloner le dépôt :**

    ```bash
    git clone https://github.com/abdemeh/PlateformeRGPD.git
    cd PlateformeRGPD/frontend
    ```

2. **Installer les dépendances :**

    Exécuter la commande suivante pour installer les dépendances nécessaires :

    ```bash
    npm install
    ```

## Utilisation

1. **Lancer le serveur de développement :**

    Depuis le dossier `frontend`, démarrer le serveur avec la commande suivante :

    ```bash
    npm run dev
    ```

    Le frontend est accessible à l'adresse [http://localhost:5173](http://localhost:5173).

2. **Interagir avec la plateforme :**

    - Télécharger un fichier CSV via l'interface utilisateur.
    - Configurer les méthodes d'anonymisation souhaitées.
    - Télécharger le fichier anonymisé généré.

## Fonctionnalités Principales

- 🌐 **Interface utilisateur intuitive** : Permet de configurer facilement les paramètres d'anonymisation.
- 📂 **Gestion des fichiers CSV** : Téléchargement et affichage des fichiers.
- 🔄 **Communication avec le backend** : Envoi des fichiers et réception des résultats via des requêtes API REST.
- ⚙️ **Extensibilité** : Possibilité d'ajouter de nouvelles pages ou fonctionnalités React.