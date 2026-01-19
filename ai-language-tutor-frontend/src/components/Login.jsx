import { useState } from "react";

const API_URL = import.meta.env.VITE_API_URL;

export default function Login({ onLogin }) {
  const [name, setName] = useState("");

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
      <h1>🌍 AI Language Tutor</h1>
      <p>Jelentkezz be a tanuláshoz!</p>

      <form onSubmit={handleSubmit} style={{ marginTop: "2rem" }}>
        <input
          type="text"
          placeholder="Neved"
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
          Belépés
        </button>
      </form>
    </div>
  );
}