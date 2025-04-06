import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import BenchmarkModal from "./components/BenchmarkModal"; // 👈 importe le modal

export default function WelcomePage() {
  const navigate = useNavigate();
  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <main className="min-h-screen text-white relative">
      {/* Header */}
      <header className="flex items-center justify-between px-6 md:px-16 py-6 border-b border-gray-700">
        <div className="header-logo-container">
          <img src="images/logo-main-2.png" alt="logo" />
        </div>
        <div className="space-x-4 flex">
          <button onClick={() => navigate("/anonymize")} className="px-4 py-2">
            Tester
          </button>
          <button onClick={() => setIsModalOpen(true)} className="px-4 py-2">
            Benchmarking
          </button>
          <button
            onClick={() =>
              window.open("https://github.com/abdemeh/PlateformeRGPD", "_blank", "noopener,noreferrer")
            }
            className="px-4 py-2"
          >
            Github
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
      <footer className="border-t border-gray-700 py-6 text-center text-sm">
        <div className="flex justify-center items-center gap-2">
          <img src="images/cytech.png" alt="Cytech Logo" className="h-[45px]" />
          <span>&copy; {new Date().getFullYear()} TraceLess Platform. Tous droits réservés.</span>
        </div>
      </footer>

      {/* Benchmark Modal */}
      {isModalOpen && <BenchmarkModal onClose={() => setIsModalOpen(false)} />}
    </main>
  );
}
