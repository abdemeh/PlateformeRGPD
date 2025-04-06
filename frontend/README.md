# TraceLess Platform – Frontend

Interface web du projet **TraceLess Platform**, une application de démonstration pour l’anonymisation de jeux de données personnels, conforme au RGPD.  
Elle permet d’uploader un fichier `.csv`, de définir des types de colonnes, et d’appliquer différentes techniques d’anonymisation.

---

## 🚀 Fonctionnalités

- 🔐 Anonymisation des données avec masquage, pseudonymisation, généralisation, perturbation, agrégation.
- 📊 Visualisation des benchmarks de performance sur des datasets de différentes tailles.
- 📁 Import facile de fichiers CSV.
- 🎨 Interface responsive et sombre avec design personnalisé (Tailwind CSS + custom CSS).
- ✅ Routing SPA avec React Router.

---

## 🧰 Technologies

- [React](https://reactjs.org/)
- [React Router](https://reactrouter.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Tabler Icons](https://tabler-icons.io/)
- HTML5 / CSS3 (custom theme + dark mode)

---

## 📂 Structure

```
📁 frontend/
├── public/
│   │── images/
│   └── fonts/
├── src/
│   ├── components/
│   │   ├── Header.jsx
│   │   ├── Footer.jsx
│   │   └── BenchmarkModal.jsx
│   ├── App.jsx
│   ├── main.jsx
│   ├── WelcomePage.jsx
│   ├── AnonymizationPage.jsx
│   └── index.css
└── README.md
```

---

## ▶️ Lancer l'application

### 1. Prérequis
- Node.js ≥ 18.x
- npm ≥ 9.x

### 2. Installation

```bash
cd frontend
npm install
```

### 3. Démarrage en local

```bash
npm run dev
```

L’application sera disponible à l'adresse : [http://localhost:5173](http://localhost:5173)

---

## 📦 Scripts utiles

| Commande           | Description                   |
|--------------------|-------------------------------|
| `npm run dev`      | Lancer le serveur de dev      |
| `npm run build`    | Build de production           |
| `npm run preview`  | Preview du build              |

---

## 📸 Aperçu

<p align="center">
  <img src="https://i.postimg.cc/PqC76532/Screenshot-2025-04-06-084829.png" alt="Screenshot 1" style="height: 200px; margin: 10px;" />
  <img src="https://i.postimg.cc/NjJV7H4K/Screenshot-2025-04-06-084813.png" alt="Screenshot 2" style="height: 200px; margin: 10px;" />
  <img src="https://i.postimg.cc/zGX6gjnm/Screenshot-2025-04-06-084820.png" alt="Screenshot 3" style="height: 200px; margin: 10px;" />
  <img src="https://i.postimg.cc/qMGWqY6X/Screenshot-2025-04-06-084858.png" alt="Screenshot 4" style="height: 200px; margin: 10px;" />
</p>

---