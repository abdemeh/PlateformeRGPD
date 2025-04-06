# PlateformeRGPD - Plateforme d'Anonymisation de Données

Ce projet fournit une plateforme permettant d'anonymiser des données sensibles contenues dans des fichiers CSV. Plusieurs méthodes d'anonymisation sont disponibles, telles que le masquage, la pseudonymisation, la généralisation, la perturbation et l'agrégation.

## Table des matières

- [Structure du Projet](#structure-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Fonctionnalités Principales](#fonctionnalités-principales)

## Structure du Projet

La structure du dossier du projet est la suivante :

```
PLATFORMERGD/
│
├── backend/                         # Backend Python (API Flask)
│   ├── app.py                       # Point d’entrée de l’API Flask
│   ├── uploads/                     # Fichiers CSV uploadés par l'utilisateur
│   ├── Benchmark/                   # Système de benchmark RGPD
│   │   ├── benchmarks/              # Modules pour évaluer les méthodes (temps, mémoire, précision, etc.)
│   │   │   └── *.py
│   │   ├── methods/                 # Implémentation des méthodes d’anonymisation
│   │   │   └── *.py
│   │   ├── utils/                   # Fonctions utilitaires (chargement, export, visualisation)
│   │   │   └── *.py
│   ├── generate.py                  # Générateur de dataset ou exécution automatique
│   ├── benchmark_summary.json       # Résultats des benchmarks
│   ├── Benchmark Report.docx        # Rapport documentaire
│   └── README.md                    # Explication du backend
│
├── frontend/                        # Frontend React (SPA)
│   ├── public/                      # Dossier public (images, polices, etc.)
│   │   ├── fonts/
│   │   └── images/
│   ├── src/                         # Source principale React
│   │   ├── components/              # Composants réutilisables
│   │   │   ├── Header.jsx
│   │   │   ├── Footer.jsx
│   │   │   └── BenchmarkModal.jsx
│   │   ├── App.jsx                  # Routing principal
│   │   ├── main.jsx                 # Point d’entrée React
│   │   ├── WelcomePage.jsx          # Page d’accueil de la plateforme
│   │   ├── AnonymizationPage.jsx    # Interface d’anonymisation des fichiers
│   │   └── index.css                # Styles globaux (custom + Tailwind)
│   ├── index.html                   # Template HTML Vite
│   ├── vite.config.js               # Configuration Vite.js
│   ├── tailwind.config.cjs          # Configuration Tailwind CSS
│   ├── postcss.config.cjs           # Config PostCSS
│   ├── package.json                 # Dépendances frontend
│   └── README.md                    # Explication du frontend
│
├── .gitignore                       # Fichiers/dossiers ignorés par Git
├── README.md                        # README global

```

## Installation

1. **Cloner le dépôt :**

    ```bash
    git clone https://github.com/abdemeh/PlateformeRGPD.git
    cd PlateformeRGPD
    ```

2. **Configurer le backend :**

    Accéder au dossier `backend` et installer les dépendances Python nécessaires :

    ```bash
    cd backend
    pip install flask flask_cors
    ```

3. **Configurer le frontend :**

    Accéder au dossier `frontend` et installer les dépendances npm :

    ```bash
    cd frontend
    npm install
    ```

## Utilisation

1. **Lancer le backend :**

    Depuis le dossier `backend`, démarrer le serveur Flask :

    ```bash
    python app.py
    ```

    Le backend est accessible à l'adresse [http://localhost:5000](http://localhost:5000).

2. **Lancer le frontend :**

    Depuis le dossier `frontend`, démarrer le serveur de développement React :

    ```bash
    npm run dev
    ```

    Le frontend est accessible à l'adresse [http://localhost:5173](http://localhost:5173).

3. **Utiliser la plateforme :**

    - Télécharger un fichier CSV via l'interface utilisateur.
    - Configurer les méthodes d'anonymisation souhaitées.
    - Télécharger le fichier anonymisé généré.

## Fonctionnalités Principales

- 📂 **Gestion des fichiers CSV** : Téléchargement, traitement et anonymisation des fichiers.
- 🔐 **Méthodes d'anonymisation disponibles** :
  - Masquage
  - Pseudonymisation
  - Généralisation
  - Perturbation
  - Agrégation
- 🌐 **Interface utilisateur intuitive** : Configuration facile des paramètres d'anonymisation.
- 🔄 **Communication backend-frontend** : Utilisation d'API REST pour transmettre les fichiers et les résultats.
- ⚙️ **Architecture modulaire** : Séparation claire entre le backend (logique métier) et le frontend (interface utilisateur).
