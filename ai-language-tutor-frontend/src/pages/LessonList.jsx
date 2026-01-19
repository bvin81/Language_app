import { useEffect, useState } from "react";
import { getLessons } from "../api/lessonApi";

export default function LessonList({ onSelectLesson }) {
  const [lessons, setLessons] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getLessons()
      .then((data) => {
        console.log("API válasz:", data);
        setLessons(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Hiba:", error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Betöltés...</div>;
  }

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Leckék</h1>

      <div style={{ marginBottom: "1rem" }}>
        <button onClick={() => window.location.reload()}>
          🔄 Frissítés
        </button>
      </div>

      {lessons.length === 0 ? (
        <div>
          <p>Még nincsenek leckék az adatbázisban.</p>
          <p>Futtasd: <code>python -m app.init_db</code></p>
        </div>
      ) : (
        <div style={{ display: "grid", gap: "1rem" }}>
          {lessons.map((lesson) => (
            <div
              key={lesson.id}
              style={{
                border: "1px solid #ddd",
                borderRadius: "8px",
                padding: "1.5rem",
                backgroundColor: lesson.is_premium ? "#fff7ed" : "#f0fdf4",
              }}
            >
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "start" }}>
                <div>
                  <h3 style={{ margin: "0 0 0.5rem 0" }}>
                    {lesson.title}
                    {lesson.is_premium && (
                      <span style={{
                        marginLeft: "0.5rem",
                        fontSize: "0.8rem",
                        color: "#ea580c",
                        fontWeight: "bold"
                      }}>
                        👑 PRÉMIUM
                      </span>
                    )}
                  </h3>
                  <p style={{ margin: "0 0 0.5rem 0", color: "#666" }}>
                    {lesson.description}
                  </p>
                  <p style={{ margin: 0, fontSize: "0.9rem", color: "#888" }}>
                    🌍 {lesson.language} • 📊 {lesson.level}
                  </p>
                </div>
                <button
                  onClick={() => onSelectLesson && onSelectLesson(lesson.id)}
                  style={{
                    padding: "0.5rem 1rem",
                    fontSize: "1rem",
                    cursor: "pointer",
                    backgroundColor: lesson.is_premium ? "#fb923c" : "#4ade80",
                    color: "#fff",
                    border: "none",
                    borderRadius: "6px",
                  }}
                  disabled={lesson.is_premium}
                >
                  {lesson.is_premium ? "🔒 Zárva" : "🎮 Játék"}
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}