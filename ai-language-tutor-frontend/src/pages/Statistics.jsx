import { useEffect, useState } from "react";

const API_URL = import.meta.env.VITE_API_URL;

export default function Statistics({ user }) {
  const [progress, setProgress] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${API_URL}/progress/${user.id}`)
      .then(res => res.json())
      .then(data => {
        setProgress(data);
        setLoading(false);
      })
      .catch(error => {
        console.error("Hiba:", error);
        setLoading(false);
      });
  }, [user.id]);

  if (loading) {
    return <div style={{ padding: "2rem" }}>Betöltés...</div>;
  }

  const totalGames = progress.length;
  const avgScore = totalGames > 0
    ? Math.round(progress.reduce((sum, p) => sum + p.percentage, 0) / totalGames)
    : 0;

  return (
    <div style={{ padding: "2rem", maxWidth: "800px", margin: "0 auto" }}>
      <h1>📊 Statisztikák</h1>

      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))",
        gap: "1rem",
        marginBottom: "2rem"
      }}>
        <div style={{
          padding: "1.5rem",
          backgroundColor: "#f0fdf4",
          borderRadius: "8px",
          textAlign: "center"
        }}>
          <div style={{ fontSize: "2rem", fontWeight: "bold", color: "#16a34a" }}>
            {totalGames}
          </div>
          <div style={{ color: "#666" }}>Játszott játék</div>
        </div>

        <div style={{
          padding: "1.5rem",
          backgroundColor: "#eff6ff",
          borderRadius: "8px",
          textAlign: "center"
        }}>
          <div style={{ fontSize: "2rem", fontWeight: "bold", color: "#2563eb" }}>
            {avgScore}%
          </div>
          <div style={{ color: "#666" }}>Átlagos eredmény</div>
        </div>
      </div>

      <h2>Előzmények</h2>

      {progress.length === 0 ? (
        <p>Még nincs egyetlen játékod sem. Kezdj el tanulni!</p>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
          {progress.map((p, index) => (
            <div
              key={index}
              style={{
                padding: "1rem",
                border: "1px solid #ddd",
                borderRadius: "8px",
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center"
              }}
            >
              <div>
                <div style={{ fontWeight: "bold" }}>Lecke #{p.lesson_id}</div>
                <div style={{ fontSize: "0.9rem", color: "#666" }}>
                  {new Date(p.completed_at).toLocaleString('hu-HU')}
                </div>
              </div>
              <div style={{ textAlign: "right" }}>
                <div style={{
                  fontSize: "1.5rem",
                  fontWeight: "bold",
                  color: p.percentage >= 80 ? "#16a34a" : p.percentage >= 50 ? "#ea580c" : "#dc2626"
                }}>
                  {p.percentage}%
                </div>
                <div style={{ fontSize: "0.9rem", color: "#666" }}>
                  {p.score} / {p.total}
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}