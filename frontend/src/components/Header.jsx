// components/Header.jsx
import React from "react";
import { Link, useNavigate } from "react-router-dom";

export default function Header({ onBenchmarkClick }) {
  const navigate = useNavigate();

  return (
    <header className="flex items-center justify-between px-6 md:px-16 py-6 border-b border-gray-700">
      <div className="header-logo-container">
      <Link to="/" className="header-logo-container">
        <img src="images/logo-main-2.png" alt="logo" />
      </Link>
      </div>
      <div className="space-x-4 flex">
        <button onClick={() => navigate("/anonymize")} className="px-4 py-2">
          Tester
        </button>
        {onBenchmarkClick && (
          <button onClick={onBenchmarkClick} className="px-4 py-2">
            Benchmarking
          </button>
        )}
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
  );
}
