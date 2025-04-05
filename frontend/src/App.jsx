import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import WelcomePage from "./WelcomePage";
import AnonymizationPage from "./AnonymizationPage";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<WelcomePage />} />
                <Route path="/anonymize" element={<AnonymizationPage />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
