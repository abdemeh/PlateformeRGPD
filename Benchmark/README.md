# Benchmark - Benchmarking des Techniques d'Anonymisation

Ce projet a pour objectif de comparer et de mesurer l'efficacité de différentes méthodes d'anonymisation de données (masquage, pseudonymisation, généralisation, perturbation, agrégation) en utilisant plusieurs critères de performance. Il permet d'effectuer des benchmarks sur des jeux de données synthétiques générés en 10k, 100k et 1M lignes, et de visualiser les résultats via des graphiques modernes.

## Table des matières

- [Structure du Projet](#structure-du-projet)
- [Génération des Datasets](#génération-des-datasets)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Fonctionnalités Principales](#fonctionnalités-principales)
- [Développement et Extension](#développement-et-extension)

## Structure du Projet

La structure du dossier du projet est la suivante :

```
Benchmark/
├── main.py                          # Script principal pour lancer les benchmarks et générer les visualisations.
├── generate.py                      # Script pour générer des datasets synthétiques (10k, 100k, 1M).
├── benchmarks/                      # Modules de calcul des critères de benchmark.
│   ├── execution_time.py
│   ├── memory_usage.py
│   ├── information_loss.py
│   ├── reversibility.py
│   ├── re_identification.py
│   ├── entropy_diversity.py
│   ├── data_precision.py
│   └── scalability.py
├── methods/                         # Méthodes d’anonymisation.
│   ├── masquage.py
│   ├── pseudonymisation.py
│   ├── generalisation.py
│   ├── perturbation.py
│   └── aggregation.py
├── utils/                           # Fonctions utilitaires.
│   ├── dataset_loader.py
│   ├── visualization.py
│   └── json_exporter.py
├── datasets/                        # Datasets originaux (non anonymisés).
│   ├── dataset_example_10000.csv
│   ├── dataset_example_100000.csv
│   └── dataset_example_1000000.csv
└── anonymized_datasets/             # Datasets anonymisés (générés automatiquement).
```

## Installation

1. **Cloner le dépôt :**

```bash
git clone https://github.com/abdemeh/PlateformeRGPD.git
cd PlateformeRGPD
cd Benchmark
```

2. **Installer les dépendances :**

```bash
pip install pandas numpy faker psutil python-Levenshtein scipy matplotlib seaborn plotly altair
```

## Génération des Datasets

Pour générer les datasets de 10k, 100k et 1M lignes, exécute simplement :

```bash
python generate.py
```

Les fichiers générés seront sauvegardés automatiquement dans le dossier `datasets/`.

## Utilisation

1. **Exécution du benchmark principal :**

```bash
python main.py
```

2. **Choisissez un dataset :**  
   Le script affichera la liste des fichiers `.csv` disponibles dans `datasets/`.

3. **Lancement de l'anonymisation + benchmark :**  
   Pour chaque méthode, un nouveau fichier anonymisé est sauvegardé dans `anonymized_datasets/`.  
   Des métriques sont calculées automatiquement, puis affichées dans des graphiques.

4. **Export JSON :**  
   Un fichier JSON est généré pour résumer tous les résultats de benchmark.

## Fonctionnalités Principales

- 📊 **Visualisation complète des benchmarks**  
  Comparaison par métrique (temps, mémoire, précision, etc.) avec graphiques modernes.

- 🔐 **Méthodes d’anonymisation testées** :
  - Masquage
  - Pseudonymisation
  - Généralisation
  - Perturbation
  - Agrégation

- 🧪 **Critères de Benchmark évalués** :
  - Temps d'exécution
  - Mémoire utilisée
  - Perte d'information
  - Réversibilité
  - Risque de ré-identification
  - Entropie / diversité
  - Précision des données
  - Robustesse à l’échelle (10k, 100k, 1M)

- 📂 **Séparation claire des données** :
  - `datasets/` contient les jeux de données initiaux.
  - `anonymized_datasets/` contient les résultats anonymisés.

- 📤 **Export des résultats en JSON** pour une analyse ou réutilisation future.

## Développement et Extension

- Ajouter une nouvelle **méthode** : créez un fichier dans `methods/`, implémentez la transformation, et ajoutez-la au dictionnaire `methods` dans `main.py`.

- Ajouter un **nouveau critère** : ajoutez une fonction dans `benchmarks/` et intégrez-la dans `run_benchmarks()`.

- Personnalisez la **visualisation** dans `utils/visualization.py`.
