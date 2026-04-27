import { useEffect, useState } from "react";
import { useLanguage } from "../i18n/LanguageContext";

const API_URL = import.meta.env.VITE_API_URL;

export default function Statistics({ user }) {
  const [progress, setProgress] = useState([]);
  const [loading, setLoading] = useState(true);
  const { t } = useLanguage();

  useEffect(() => {
    fetch(`${API_URL}/progress/${user.id}`)
      .then(res => res.json())
      .then(data => { setProgress(data); setLoading(false); })
      .catch(error => { console.error("Error:", error); setLoading(false); });
  }, [user.id]);

  if (loading) return <div style={{ padding: "2rem" }}>{t.loading}</div>;

  const totalGames = progress.length;
  const avgScoreVal = totalGames > 0
    ? Math.round(progress.reduce((sum, p) => sum + p.percentage, 0) / totalGames)
    : 0;

  return (
    <div style={{ padding: "2rem", maxWidth: "800px", margin: "0 auto" }}>
      <h1>📊 {t.navStatistics.replace("📊 ", "")}</h1>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: "1rem", marginBottom: "2rem" }}>
        <div style={{ padding: "1.5rem", backgroundColor: "#f0fdf4", borderRadius: "8px", textAlign: "center" }}>
          <div style={{ fontSize: "2rem", fontWeight: "bold", color: "#16a34a" }}>{totalGames}</div>
          <div style={{ color: "#666" }}>{t.gamesPlayed}</div>
        </div>
        <div style={{ padding: "1.5rem", backgroundColor: "#eff6ff", borderRadius: "8px", textAlign: "center" }}>
          <div style={{ fontSize: "2rem", fontWeight: "bold", color: "#2563eb" }}>{avgScoreVal}%</div>
          <div style={{ color: "#666" }}>{t.avgScore}</div>
        </div>
      </div>

      <h2>{t.history}</h2>

      {progress.length === 0 ? (
        <p>{t.noGames}</p>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
          {progress.map((p, index) => (
            <div key={index} style={{ padding: "1rem", border: "1px solid #ddd", borderRadius: "8px", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <div>
                <div style={{ fontWeight: "bold" }}>{t.lessonHash}{p.lesson_id}</div>
                <div style={{ fontSize: "0.9rem", color: "#666" }}>
                  {new Date(p.completed_at).toLocaleString(t.locale)}
                </div>
              </div>
              <div style={{ textAlign: "right" }}>
                <div style={{ fontSize: "1.5rem", fontWeight: "bold", color: p.percentage >= 80 ? "#16a34a" : p.percentage >= 50 ? "#ea580c" : "#dc2626" }}>
                  {p.percentage}%
                </div>
                <div style={{ fontSize: "0.9rem", color: "#666" }}>{p.score} / {p.total}</div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
