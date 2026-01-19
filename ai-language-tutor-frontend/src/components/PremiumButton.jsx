import { useState } from "react";

const API_URL = import.meta.env.VITE_API_URL;

export default function PremiumButton({ user, onUpgrade }) {
  const [loading, setLoading] = useState(false);

  const handleUpgrade = async () => {
    setLoading(true);

    const res = await fetch(`${API_URL}/users/${user.id}/upgrade-premium`, {
      method: "POST"
    });

    const updatedUser = await res.json();
    localStorage.setItem("user", JSON.stringify(updatedUser));
    onUpgrade(updatedUser);
    setLoading(false);
  };

  if (user.is_premium) {
    return <span>👑 Prémium tag</span>;
  }

  return (
    <button
      onClick={handleUpgrade}
      disabled={loading}
      style={{
        padding: "0.5rem 1rem",
        backgroundColor: "#f59e0b",
        color: "white",
        border: "none",
        borderRadius: "8px",
        cursor: loading ? "default" : "pointer",
        fontWeight: "bold"
      }}
    >
      {loading ? "..." : "👑 Válj Prémium tagga!"}
    </button>
  );
}