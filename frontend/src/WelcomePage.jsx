import React from "react";
import { useNavigate } from "react-router-dom";

function WelcomePage() {
    const navigate = useNavigate();

    const handleTestClick = () => {
        navigate("/anonymize");
    };

    return (
        <div className="min-h-screen bg-black text-white flex flex-col items-center justify-center px-4 py-12">
            <h1 className="text-4xl md:text-5xl font-bold text-lime-400 mb-6 text-center">
                Bienvenue sur TraceLess Platform
            </h1>
            <p className="text-lg text-center max-w-3xl mb-10">
                Découvrez notre plateforme d'anonymisation de données conforme au RGPD.
                Protégez les données personnelles de vos utilisateurs grâce à des
                techniques avancées : masquage, pseudonymisation, perturbation, etc.
            </p>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-6xl w-full">
                {/* Card 1 */}
                <div className="bg-gray-900 rounded-2xl shadow-lg overflow-hidden p-4 flex flex-col items-center">
                    <div className="max-w-sm w-full mx-auto border-4 border-red-500">
                        <img
                            src="/img_2.png"
                            alt="Étapes de pseudonymisation"
                            className="w-full h-auto object-contain"
                        />
                    </div>
                    <div className="mt-4 text-center">
                        <h2 className="text-xl text-lime-300 font-semibold">
                            Masquage de noms et e-mails
                        </h2>
                        <p className="text-sm mt-2">
                            Exemple d'anonymisation partielle de données sensibles dans un fichier client.
                        </p>
                    </div>
                </div>

                {/* Card 2 */}
                <div className="bg-gray-900 rounded-2xl shadow-lg overflow-hidden p-4 flex flex-col items-center">
                    <div className="max-w-sm mx-auto w-full">
                        <img
                            src="/img_3.png"
                            alt="Étapes de pseudonymisation"
                            className="w-full h-auto object-contain"
                        />
                    </div>
                    <div className="mt-4 text-center">
                        <h2 className="text-xl text-lime-300 font-semibold">
                            Généralisation de dates et salaires
                        </h2>
                        <p className="text-sm mt-2">
                            Visualisation d'une anonymisation par plage d'âges et fourchettes de salaires.
                        </p>
                    </div>
                </div>
            </div>

            <div className="bg-gray-900 rounded-2xl shadow-lg w-full max-w-screen-xl mx-auto mb-10 px-4 py-6 flex flex-col items-center">
                <div className="max-w-sm mx-auto w-full">
                    <img
                        src="/img.png"
                        alt="Schéma RGPD"
                        className="w-full h-auto object-contain"
                    />
                </div>
                <div className="p-4 text-center">
                    <h2 className="text-xl text-lime-300 font-semibold">
                        Schéma de confidentialité RGPD
                    </h2>
                    <p className="text-sm mt-2">
                        Illustration du lien entre données confidentielles et éléments identifiants.
                    </p>
                </div>
            </div>

            <div
                className="bg-gray-900 rounded-2xl shadow-lg w-full max-w-screen-xl mx-auto mb-10 px-4 py-6 flex flex-col items-center">
                <div className="max-w-sm w-full mx-auto border-4 border-red-500">
                    <img
                        src="/img_1.png"
                        alt="Étapes de pseudonymisation"
                        className="w-full h-auto object-contain"
                    />
                </div>
                <div className="p-4 text-center">
                    <h2 className="text-xl text-lime-300 font-semibold">
                        Étapes de la pseudonymisation
                    </h2>
                    <p className="text-sm mt-2">
                        Processus complet : collecte, identification, pseudonymisation, stockage et réutilisation
                        sécurisée.
                    </p>
                </div>
            </div>

            <button
                onClick={handleTestClick}
                className="mt-10 px-8 py-3 bg-lime-400 text-black text-lg font-semibold rounded-full hover:bg-lime-300 transition"
            >
                Tester la plateforme
            </button>
        </div>
    );
}

export default WelcomePage;
