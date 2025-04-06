import React, { useState } from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import BenchmarkModal from "./components/BenchmarkModal";

function AnonymizationPage() {
  const [file, setFile] = useState(null);
  const [columns, setColumns] = useState([]);
  const [csvData, setCsvData] = useState([]);
  const [columnTypes, setColumnTypes] = useState({});
  const [columnMethods, setColumnMethods] = useState({});
  const [anonymizedData, setAnonymizedData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const typeToMethods = {
    name: ["masking", "pseudonymization"],
    email: ["masking", "pseudonymization"],
    telephone: ["masking", "perturbation"],
    carte_bancaire: ["masking"],
    pays: ["generalization"],
    genre: [],
    date_naissance: ["generalization", "perturbation"],
    age: ["generalization", "perturbation"],
    chiffre: ["perturbation", "generalization", "aggregation"],
    solde: ["masking", "perturbation", "generalization", "aggregation"],
    revenu: ["masking", "perturbation", "generalization", "aggregation"],
    salaire: ["masking", "perturbation", "generalization", "aggregation"],
    ville: ["generalization"],
    adresse: ["masking", "generalization"],
    autre: ["masking", "pseudonymization", "perturbation", "generalization", "aggregation"],
    id: [],
  };

  const handleFileUpload = (event) => {
    const uploadedFile = event.target.files[0];
    if (uploadedFile && uploadedFile.type === "text/csv") {
      setFile(uploadedFile);
      const reader = new FileReader();
      reader.onload = () => {
        const text = reader.result;
        const rows = text.split("\n").map((row) => row.split(","));
        const headers = rows[0].map((h) => h.trim());
        setColumns(headers);
        setCsvData(rows.slice(1));
      };
      reader.readAsText(uploadedFile);
    } else {
      alert("Veuillez choisir un fichier CSV");
    }
  };

  const handleTypeChange = (e, column) => {
    const type = e.target.value;
    setColumnTypes((prev) => ({ ...prev, [column]: type }));
    setColumnMethods((prev) => ({ ...prev, [column]: "" }));
  };

  const handleMethodChange = (e, column) => {
    const method = e.target.value;
    setColumnMethods((prev) => ({ ...prev, [column]: method }));
  };

  const handleAnonymization = async () => {
    if (!file) return alert("Veuillez choisir un fichier CSV");

    const formData = new FormData();
    formData.append("file", file);

    columns.forEach((col) => {
      const type = columnTypes[col];
      const method = columnMethods[col];
      if (type) formData.append(`${col}_type`, type);
      if (method) formData.append(`${col}_method`, method);
    });

    setLoading(true);
    setError(null);
    try {
      const res = await fetch("http://localhost:5000/anonymize", {
        method: "POST",
        body: formData,
      });

      if (!res.ok) throw new Error("Erreur lors de l’anonymisation");

      const text = await res.text();
      setAnonymizedData(text);
    } catch (err) {
      console.error(err);
      setError(err.message || "Erreur inconnue");
    } finally {
      setLoading(false);
    }
  };

  const downloadCSV = () => {
    const blob = new Blob([anonymizedData], { type: "text/csv" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "anonymized_data.csv";
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <>
      <Header onBenchmarkClick={() => setIsModalOpen(true)} />
      <section className="text-center pt-20 px-6 md:px-0">
        <h1 className="text-4xl md:text-6xl font-bold mb-6 leading-tight">
          <span className="text-primary">Anonym</span>iser vos données
        </h1>
        <p className="max-w-2xl mx-auto text-lg mb-10">
        Importez votre fichier CSV et appliquez automatiquement les techniques d’anonymisation adaptées à chaque type de donnée.
        </p>
      </section>
      <div className="p-6 max-w-4xl mx-auto">
      <input
        type="file"
        accept=".csv"
        onChange={handleFileUpload}
      />
        {columns.length > 0 && (
          <div className="grid md:grid-cols-2 gap-2 max-w-6xl mx-auto px-2">
            {columns.map((col) => (
              <div key={col} className="select-div p-4">
                <h3 className="font-semibold">{col}</h3>
                <div className="flex flex-col sm:flex-row sm:items-center gap-2 mt-2">
                  <select
                    value={columnTypes[col] || ""}
                    onChange={(e) => handleTypeChange(e, col)}
                    className="p-2"
                  >
                    <option value="">Sélectionner le type</option>
                    {Object.keys(typeToMethods).map((type) => (
                      <option key={type} value={type}>
                        {type}
                      </option>
                    ))}
                  </select>

                  {columnTypes[col] && (
                    <select
                      value={columnMethods[col] || ""}
                      onChange={(e) => handleMethodChange(e, col)}
                      className="p-2"
                    >
                      <option value="">Méthode à appliquer</option>
                      {typeToMethods[columnTypes[col]].map((method) => (
                        <option key={method} value={method}>
                          {method}
                        </option>
                      ))}
                    </select>
                  )}
                </div>
              </div>
            ))}
          </div>
        )}
        <div className="flex justify-center mt-6">
          <button
            onClick={handleAnonymization}
            disabled={loading}
            className="mt-2 px-4 py-2 w-60"
          >
            {loading ? "Traitement en cours..." : "Anonimiser les données"}
          </button>
        </div>
        {error && <p className="text-red-500 mt-4">{error}</p>}

        {anonymizedData && (
          <div className="flex justify-center">
            <button
              onClick={downloadCSV}
              className="px-4 py-2 w-60"
            >
              Télécharger
            </button>
          </div>
        )}
      </div>

      {isModalOpen && <BenchmarkModal onClose={() => setIsModalOpen(false)} />}

      <Footer />
    </>
  );
}

export default AnonymizationPage;
