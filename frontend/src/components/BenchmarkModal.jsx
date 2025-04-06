import React, { useState, useEffect } from "react";

const benchmarks = [
  {
    title: "🟢 Benchmark - 10 000 lignes",
    img: "images/benchmark_10k.png",
    desc: "Toutes les méthodes s’exécutent rapidement. Agrégation offre un excellent équilibre entre précision et rapidité.",
    color: "text-green-400",
  },
  {
    title: "🟡 Benchmark - 100 000 lignes",
    img: "images/benchmark_100k.png",
    desc: "La mémoire devient importante. Perturbation et agrégation restent stables et efficaces.",
    color: "text-yellow-400",
  },
  {
    title: "🔴 Benchmark - 1 000 000 lignes",
    img: "images/benchmark_1m.png",
    desc: "À grande échelle, perturbation reste précise mais gourmande. Agrégation est toujours stable.",
    color: "text-red-400",
  },
];

export default function BenchmarkModal({ onClose }) {
  const [index, setIndex] = useState(0);
  const [fade, setFade] = useState(true);

  const goTo = (i) => {
    if (i === index) return;
    setFade(false);
    setTimeout(() => {
      setIndex(i);
      setFade(true);
    }, 200); // match duration of fade-out
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div
        className="modal-content max-w-4xl w-full p-8 overflow-hidden relative"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <h2 className="text-3xl font-bold text-center mb-4">📊 Résultats de Benchmarking</h2>

        {/* Slide content*/}
        <div className={`transition-opacity duration-200 ${fade ? "opacity-100" : "opacity-0"}`}>
          <h3 className={`text-xl font-semibold mb-2 text-center ${benchmarks[index].color}`}>
            {benchmarks[index].title}
          </h3>
          <img
            src={benchmarks[index].img}
            alt={benchmarks[index].title}
            className="w-full rounded-xl shadow-lg border border-gray-700"
          />
          <p className="text-sm text-gray-400 mt-4 text-center">
            {benchmarks[index].desc}
          </p>
        </div>

        {/* Dots navigation */}
        <div className="flex justify-center mt-6 space-x-2">
          {benchmarks.map((_, i) => (
            <button
              key={i}
              onClick={() => goTo(i)}
              className={`w-2.5 h-2.5 p-0 m-0 min-w-0 min-h-0 rounded-full border-2 ${
                i === index
                  ? "bg-[var(--primary-color)] border-[var(--primary-color)]"
                  : "bg-transparent border-[var(--primary-color)]"
              } transition duration-300 hover:bg-[var(--primary-color)]`}
              style={{ padding: 0 }}
            />
          ))}
        </div>

        {/* Close button */}
        <div className="flex justify-center mt-8">
          <button onClick={onClose} className="px-6 py-2">
            Fermer
          </button>
        </div>
      </div>
    </div>
  );
}
