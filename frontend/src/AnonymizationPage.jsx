import React, { useState } from "react";

function AnonymizationPage() {
    const [file, setFile] = useState(null);
    const [anonymizedData, setAnonymizedData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [columns, setColumns] = useState([]);
    const [finiteValueColumns, setFiniteValueColumns] = useState([]);
    const [generalizations, setGeneralizations] = useState({});
    const [columnTypes, setColumnTypes] = useState({});  // Etat pour les types de colonnes
    const [csvData, setCsvData] = useState([]);

    const handleFileUpload = (event) => {
        const uploadedFile = event.target.files[0];

        if (uploadedFile && uploadedFile.type === "text/csv") {
            setFile(uploadedFile);
            setError(null); // Réinitialiser les erreurs
            parseCSV(uploadedFile);
        } else {
            alert("Veuillez télécharger un fichier CSV !");
        }
    };

    const parseCSV = async (uploadedFile) => {
        const reader = new FileReader();
        reader.onload = () => {
            const content = reader.result;
            const rows = content.split("\n");
            const headers = rows[0].split(",");
            setColumns(headers);

            // Fusionner les colonnes 'prenom' et 'nom' en une seule colonne 'name'
            const newHeaders = headers.map(header =>
                header.toLowerCase() === 'prenom' || header.toLowerCase() === 'nom' ? 'name' : header
            );

            setColumns(newHeaders);

            // Extraire les données pour analyse
            const data = rows.slice(1).map((row) => row.split(","));
            setCsvData(data);
        };
        reader.readAsText(uploadedFile);
    };

    const handleAnonymization = async () => {
        if (!file) {
            setError("Veuillez sélectionner un fichier.");
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        // Supprimer les colonnes identifiantes explicitement et utiliser 'name' par défaut
        formData.append("identifierColumns", "name");  // Utiliser 'name' comme identifiant unique

        // Ajouter les types de colonnes (y compris l'ID)
        for (const [col, type] of Object.entries(columnTypes)) {
            formData.append(`${col}_type`, type);
        }

        setLoading(true);
        setError(null);
        try {
            const response = await fetch("http://localhost:5000/anonymize", {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                const errorText = await response.text();
                throw new Error(errorText || "Une erreur est survenue lors de l'anonymisation");
            }

            const anonymizedText = await response.text();
            setAnonymizedData(anonymizedText);
        } catch (error) {
            console.error("Erreur:", error);
            setError(error.message);
        } finally {
            setLoading(false);
        }
    };

    const handleExport = () => {
        if (!anonymizedData) return;

        const blob = new Blob([anonymizedData], { type: "text/csv" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "anonymized_data.csv";
        a.click();
        URL.revokeObjectURL(url);
    };

    const handleFiniteValueColumnChange = (event, columnName) => {
        const { checked } = event.target;

        if (checked) {
            setFiniteValueColumns([...finiteValueColumns, columnName]);
        } else {
            setFiniteValueColumns(finiteValueColumns.filter((col) => col !== columnName));
        }
    };

    const getUniqueValuesForColumn = (columnName) => {
        const columnIndex = columns.indexOf(columnName);
        const values = csvData.map(row => row[columnIndex]);
        return [...new Set(values)]; // Extraire les valeurs uniques
    };

    const handleGeneralizationChange = (event, columnName, specificValue) => {
        const { value } = event.target;
        setGeneralizations(prevState => {
            const newGeneralizations = { ...prevState };
            if (!newGeneralizations[columnName]) {
                newGeneralizations[columnName] = {};
            }
            if (value) {
                newGeneralizations[columnName][specificValue] = value;
            } else {
                delete newGeneralizations[columnName][specificValue];
            }
            return newGeneralizations;
        });
    };

    const handleColumnTypeChange = (event, columnName) => {
        const { value } = event.target;
        setColumnTypes(prevState => ({
            ...prevState,
            [columnName]: value
        }));
    };

    return (
        <div className="p-4">
            <h1 className="text-2xl mb-4">Plateforme d'Anonymisation</h1>

            <input
                type="file"
                onChange={handleFileUpload}
                accept=".csv"
                className="mb-4"
            />

            {columns.length > 0 && (
                <div>
                    <h2>Choisissez le type de chaque colonne</h2>
                    <div>
                        {columns.map((col) => (
                            <div key={col}>
                                <label>{col}</label>
                                <select
                                    value={columnTypes[col] || ""}
                                    onChange={(e) => handleColumnTypeChange(e, col)}
                                >
                                    <option value="">Sélectionner un type</option>
                                    <option value="email">Email</option>
                                    <option value="name">Nom complet</option>
                                    <option value="telephone">Numéro de téléphone</option>
                                    <option value="id">ID</option>
                                    <option value="date_naissance">Date de naissance</option>
                                    <option value="ville">Ville</option>
                                    <option value="adresse">Adresse</option>
                                    <option value="chiffre">Chiffre</option>
                                    <option value="carte_bancaire">Numéro de carte bancaire</option> {/* Ajout du type "Carte bancaire" */}
                                    <option value="autre">Autre</option>
                                </select>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            <button
                onClick={handleAnonymization}
                className="px-4 py-2 bg-blue-500 text-white rounded mb-4"
                disabled={loading}
            >
                {loading ? "Anonymisation en cours..." : "Anonymiser les données"}
            </button>

            {error && <p className="text-red-500">{error}</p>}

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
