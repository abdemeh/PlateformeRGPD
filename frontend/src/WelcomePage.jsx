import React from "react";
import { useNavigate } from "react-router-dom";

export default function WelcomePage() {
  const navigate = useNavigate();

  return (
    <main className="min-h-screen text-white">
      {/* Header */}
      <header className="flex items-center justify-between px-6 md:px-16 py-6 border-b border-gray-700">
        <img className="header-icon" src="images/logo-main-2.png" alt="" />
        <div className="space-x-4">
          <button onClick={() => navigate("/anonymize")} className="bg-purple-500 hover:bg-purple-400 text-white px-4 py-2 rounded-lg font-medium">
            Commencer
          </button>
        </div>
      </header>

      {/* Hero Section */}
      <section className="text-center py-20 px-6 md:px-0">
        <h1 className="text-4xl md:text-6xl font-bold mb-6 leading-tight">
          Protégez vos données <br />
          avec <span className="text-primary">TraceLess Platform</span>
        </h1>
        <p className="max-w-2xl mx-auto text-lg mb-10">
          Notre plateforme d'anonymisation RGPD vous aide à sécuriser les données personnelles
          avec des méthodes avancées : pseudonymisation, masquage, généralisation...
        </p>
      </section>

      {/* Feature Cards */}
      <section className="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto px-6 pb-24">
        {[
          {
            title: "Pseudonymisation",
            desc: "Remplacez les identifiants directs par des codes uniques.",
            icon: "🔒",
          },
          {
            title: "Masquage",
            desc: "Cachez certaines informations sensibles partiellement ou totalement.",
            icon: "🕵️‍♂️",
          },
          {
            title: "Perturbation",
            desc: "Ajoutez du bruit aux données numériques pour éviter la ré-identification.",
            icon: "📊",
          },
        ].map((feat, idx) => (
          <div
            key={idx}
            className="border border-gray-700 rounded-xl p-6 text-center hover:shadow-lg transition"
          >
            <div className="text-4xl mb-4">{feat.icon}</div>
            <h3 className="text-secondary text-xl font-semibold mb-2">{feat.title}</h3>
            <p className="text-sm">{feat.desc}</p>
          </div>
        ))}
      </section>

      {/* Footer */}
      <footer className="border-t border-gray-700 py-6 text-center text-gray-500 text-sm">
        &copy; {new Date().getFullYear()} TraceLess. Tous droits réservés.
      </footer>
    </main>
  );
}
