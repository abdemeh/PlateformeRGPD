import React, { useState } from "react";

function AnonymizationPage() {
    const [file, setFile] = useState(null);
    const [data, setData] = useState(null);
    const [anonymizedData, setAnonymizedData] = useState(null);

    const handleFileUpload = (event) => {
        const uploadedFile = event.target.files[0];

        // Vérifie si le fichier est un CSV
        if (uploadedFile && uploadedFile.type === "text/csv") {
            setFile(uploadedFile);

            const reader = new FileReader();
            reader.onload = (e) => {
                setData(e.target.result);
            };
            reader.readAsText(uploadedFile);
        } else {
            alert("Veuillez télécharger un fichier CSV !");
        }
    };

    const handleAnonymization = () => {
        if (!data) return;

        // Simulation de l'anonymisation (remplace les données par "XXXX")
        const anonymized = data
            .split('\n')
            .map(line => line.split(',').map(() => "XXXX").join(','))
            .join('\n');
        setAnonymizedData(anonymized);
    };

    const handleExport = () => {
        if (!anonymizedData) return;

        // Création d'un fichier CSV
        const blob = new Blob([anonymizedData], { type: "text/csv" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "anonymized_data.csv"; // L'export se fait en .csv
        a.click();
        URL.revokeObjectURL(url);
    };

    return (
        <div className="p-4">
            <h1 className="text-2xl mb-4">Plateforme d'Anonymisation</h1>

            <input
                type="file"
                onChange={handleFileUpload}
                accept=".csv"  // Accepte uniquement les fichiers CSV
                className="mb-4"
            />

            <button
                onClick={handleAnonymization}
                className="px-4 py-2 bg-blue-500 text-white rounded mb-4"
            >
                Anonymiser les données
            </button>

            {anonymizedData && (
                <button
                    onClick={handleExport}
                    className="px-4 py-2 bg-green-500 text-white rounded"
                >
                    Exporter les données anonymisées
                </button>
            )}
        </div>
    );
}

export default AnonymizationPage;
