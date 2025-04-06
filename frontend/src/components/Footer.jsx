// components/Footer.jsx
import React from "react";

export default function Footer() {
  return (
    <footer className="border-t border-gray-700 py-6 text-center text-sm">
      <div className="flex justify-center items-center gap-2">
        <img src="images/cytech.png" alt="Cytech Logo" className="h-[45px]" />
        <span>&copy; {new Date().getFullYear()} TraceLess Platform. Tous droits réservés.</span>
      </div>
    </footer>
  );
}
