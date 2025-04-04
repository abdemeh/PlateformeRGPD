import React, { useState } from "react";

const typeToMethods = {
  name: ["masking", "pseudonymization"],
  email: ["masking", "pseudonymization"],
  phone: ["masking", "perturbation"],
  age: ["aggregation", "perturbation"],
  address: ["masking", "generalization"],
  country: ["generalization"],
  city: ["generalization"],
  date: ["generalization", "perturbation"],
  id: [],
  other: ["masking", "pseudonymization", "generalization", "perturbation", "aggregation"]
};

function AnonymizationPage() {
  const [file, setFile] = useState(null);
  const [columns, setColumns] = useState([]);
  const [preview, setPreview] = useState([]);
  const [columnTypes, setColumnTypes] = useState({});
  const [methods, setMethods] = useState({});
  const [generalizations, setGeneralizations] = useState({});
  const [excludedCols, setExcludedCols] = useState([]);
  const [metrics, setMetrics] = useState(null);
  const [downloadUrl, setDownloadUrl] = useState(null);
  const [anonymizedPreview, setAnonymizedPreview] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleFileUpload = async (e) => {
    const uploadedFile = e.target.files[0];
    if (!uploadedFile || uploadedFile.type !== "text/csv") return alert("Fichier CSV requis");

    setFile(uploadedFile);
    const reader = new FileReader();
    reader.onload = () => {
      const text = reader.result;
      const rows = text.split("\n").map((r) => r.split(","));
      setColumns(rows[0]);
      setPreview(rows.slice(1, 6));
    };
    reader.readAsText(uploadedFile);
  };

  const handleTypeChange = (col, type) => {
    setColumnTypes((prev) => ({ ...prev, [col]: type }));
    if (!typeToMethods[type]?.includes(methods[col])) {
      setMethods((prev) => ({ ...prev, [col]: "" })); // reset invalid method
    }
  };

  const handleMethodChange = (col, method) => {
    setMethods((prev) => ({ ...prev, [col]: method }));
  };

  const handleGenChange = (col, original, generalized) => {
    setGeneralizations((prev) => ({
      ...prev,
      [col]: {
        ...(prev[col] || {}),
        [original]: generalized
      }
    }));
  };

  const handleExclusionChange = (col, checked) => {
    if (checked) {
      setExcludedCols((prev) => [...prev, col]);
    } else {
      setExcludedCols((prev) => prev.filter((c) => c !== col));
    }
  };

  const submitAnonymization = async () => {
    if (!file) return;

    const form = new FormData();
    form.append("file", file);

    columns.forEach((col) => {
      if (excludedCols.includes(col)) return;
      if (methods[col]) form.append(`${col}_method`, methods[col]);
      if (methods[col] === "generalization" && generalizations[col]) {
        form.append(`${col}_generalization`, JSON.stringify(generalizations[col]));
      }
    });

    setLoading(true);
    const res = await fetch("http://localhost:5000/anonymize", {
      method: "POST",
      body: form
    });

    const data = await res.json();
    setMetrics(data);
    setDownloadUrl("http://localhost:5000" + data.download_url);

    fetch(data.download_url)
      .then((res) => res.text())
      .then((csv) => {
        const rows = csv.split("\n").map((r) => r.split(","));
        setAnonymizedPreview(rows.slice(1, 6));
      });

    setLoading(false);
  };

  return (
    <div className="p-4 max-w-5xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Anonymisation de Données CSV</h1>

      <input type="file" accept=".csv" onChange={handleFileUpload} className="mb-4" />

      {columns.length > 0 && (
        <div>
          <h2 className="text-xl mb-2">Configuration par colonne :</h2>
          {columns.map((col) => {
            const type = columnTypes[col] || "";
            const availableMethods = typeToMethods[type] || [];

            return (
              <div key={col} className="mb-4 border p-2 rounded">
                <label className="block font-semibold">{col}</label>

                <label className="block text-sm mt-1">
                  <input
                    type="checkbox"
                    checked={excludedCols.includes(col)}
                    onChange={(e) => handleExclusionChange(col, e.target.checked)}
                  />{" "}
                  Ne pas anonymiser cette colonne
                </label>

                {!excludedCols.includes(col) && (
                  <>
                    <label className="block mt-2 text-sm">Type de donnée :</label>
                    <select
                      className="border rounded p-1 w-full"
                      value={columnTypes[col] || ""}
                      onChange={(e) => handleTypeChange(col, e.target.value)}
                    >
                      <option value="">-- Sélectionner un type --</option>
                      {Object.keys(typeToMethods).map((typeOption) => (
                        <option key={typeOption} value={typeOption}>
                          {typeOption}
                        </option>
                      ))}
                    </select>

                    {type && availableMethods.length > 0 && (
                      <>
                        <label className="block mt-2 text-sm">Méthode d’anonymisation :</label>
                        <select
                          className="border rounded p-1 w-full"
                          value={methods[col] || ""}
                          onChange={(e) => handleMethodChange(col, e.target.value)}
                        >
                          <option value="">-- Aucune --</option>
                          {availableMethods.map((m) => (
                            <option key={m} value={m}>
                              {m}
                            </option>
                          ))}
                        </select>
                      </>
                    )}

                    {methods[col] === "generalization" &&
                    !(["city", "age", "date", "birthdate", "revenue", "income", "salaire"].includes(columnTypes[col])) && (
                        <div className="mt-2">
                        <label className="text-sm">Règles de généralisation :</label>
                        {Array.from(new Set(preview.map(r => r[columns.indexOf(col)]))).map(value => (
                            <div key={value} className="flex gap-2 items-center my-1">
                            <span className="text-sm w-32">{value}</span>
                            <input
                                type="text"
                                placeholder="Catégorie..."
                                className="border rounded px-2 py-1 flex-1"
                                value={generalizations[col]?.[value] || ""}
                                onChange={(e) => handleGenChange(col, value, e.target.value)}
                            />
                            </div>
                        ))}
                        </div>
                    )}
                    
                  </>
                )}
              </div>
            );
          })}

          <button
            onClick={submitAnonymization}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
            disabled={loading}
          >
            {loading ? "Anonymisation en cours..." : "Lancer l'anonymisation"}
          </button>
        </div>
      )}

      {metrics && (
        <div className="mt-6 bg-gray-100 p-4 rounded">
          <h2 className="text-xl font-semibold mb-2">📊 Métriques RGPD :</h2>
          <ul className="list-disc ml-5 text-sm">
            <li>⏱️ Temps de traitement : {metrics.processing_time} secondes</li>
            <li>🧠 Risque de ré-identification : {metrics.estimated_reidentification_risk}</li>
            <li>📊 Fidélité des données : {metrics.data_fidelity_score}%</li>
            <li>✅ Conformité RGPD : {metrics.gdpr_compliance}</li>
          </ul>
        </div>
      )}

      {preview.length > 0 && anonymizedPreview.length > 0 && (
        <div className="mt-6 grid grid-cols-2 gap-4">
          <div>
            <h3 className="font-semibold">🕵️‍♀️ Données originales (extrait)</h3>
            <table className="text-xs border border-collapse w-full mt-1">
              <tbody>
                {preview.map((row, i) => (
                  <tr key={i}>
                    {row.map((cell, j) => (
                      <td key={j} className="border p-1">{cell}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <div>
            <h3 className="font-semibold">🛡️ Données anonymisées (extrait)</h3>
            <table className="text-xs border border-collapse w-full mt-1">
              <tbody>
                {anonymizedPreview.map((row, i) => (
                  <tr key={i}>
                    {row.map((cell, j) => (
                      <td key={j} className="border p-1">{cell}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {downloadUrl && (
        <div className="mt-6">
          <h2 className="text-lg font-semibold mb-2">📥 Télécharger le fichier :</h2>
          <a
            href={downloadUrl}
            target="_blank"
            rel="noreferrer"
            className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 inline-block"
          >
            Télécharger le CSV anonymisé
          </a>
        </div>
      )}
    </div>
  );
}

export default AnonymizationPage;
