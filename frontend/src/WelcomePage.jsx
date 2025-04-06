import React, { useState } from "react";
import BenchmarkModal from "./components/BenchmarkModal";
import Header from "./components/Header";
import Footer from "./components/Footer";

import {
  IconSquareAsterisk,
  IconEyeOff,
  IconListNumbers,
} from "@tabler/icons-react";

export default function WelcomePage() {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const features = [
    {
      title: "Pseudonymisation",
      desc: "Remplacez les identifiants directs par des codes uniques.",
      icon: <IconSquareAsterisk size={40} stroke={1.5} />,
    },
    {
      title: "Masquage",
      desc: "Cachez certaines informations sensibles partiellement ou totalement.",
      icon: <IconEyeOff size={40} stroke={1.5} />,
    },
    {
      title: "Perturbation",
      desc: "Ajoutez du bruit aux données numériques pour éviter la ré-identification.",
      icon: <IconListNumbers size={40} stroke={1.5} />,
    },
  ];

  return (
    <main className="min-h-screen text-white relative">
      <Header onBenchmarkClick={() => setIsModalOpen(true)} />

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
        {features.map((feat, idx) => (
          <div
            key={idx}
            className="border border-gray-700 rounded-xl p-6 text-center hover:shadow-lg transition"
          >
            <div className="mb-4 text-primary flex justify-center">{feat.icon}</div>
            <h3 className="text-secondary text-xl font-semibold mb-2">{feat.title}</h3>
            <p className="text-sm">{feat.desc}</p>
          </div>
        ))}
      </section>

      <Footer />

      {/* Benchmark Modal */}
      {isModalOpen && <BenchmarkModal onClose={() => setIsModalOpen(false)} />}
    </main>
  );
}
