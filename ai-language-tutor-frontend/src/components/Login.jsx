import { useState } from "react";
import { useLanguage } from "../i18n/LanguageContext";

const API_URL = import.meta.env.VITE_API_URL;

export default function Login({ onLogin }) {
  const [name, setName] = useState("");
  const { t, lang, toggle } = useLanguage();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch(`${API_URL}/users/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name })
    });
    const user = await res.json();
    localStorage.setItem("user", JSON.stringify(user));
    onLogin(user);
  };

  return (
    <div style={{ maxWidth: "400px", margin: "4rem auto", padding: "2rem", textAlign: "center" }}>
      <div style={{ textAlign: "right", marginBottom: "1rem" }}>
        <button
          onClick={toggle}
          style={{
            padding: "0.4rem 0.9rem",
            backgroundColor: lang === "en" ? "#1d4ed8" : "#6b7280",
            color: "white",
            border: "none",
            borderRadius: "6px",
            cursor: "pointer",
            fontWeight: "bold",
            fontSize: "0.85rem"
          }}
        >
          {lang === "hu" ? "EN" : "HU"}
        </button>
      </div>
      <h1>🌍 AI Language Tutor</h1>
      <p>{t.loginSubtitle}</p>
      <form onSubmit={handleSubmit} style={{ marginTop: "2rem" }}>
        <input
          type="text"
          placeholder={t.yourName}
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
          style={{
            width: "100%",
            padding: "1rem",
            fontSize: "1rem",
            border: "2px solid #ddd",
            borderRadius: "8px",
            marginBottom: "1rem"
          }}
        />
        <button
          type="submit"
          style={{
            width: "100%",
            padding: "1rem",
            fontSize: "1rem",
            backgroundColor: "#3b82f6",
            color: "white",
            border: "none",
            borderRadius: "8px",
            cursor: "pointer"
          }}
        >
          {t.loginButton}
        </button>
      </form>
    </div>
  );
}
