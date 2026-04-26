import { useEffect, useState } from "react";
import { getLessons } from "../api/lessonApi";

export default function LessonList({ onSelectGame, user }) {
  const [lessons, setLessons] = useState([]);
  const [loading, setLoading] = useState(true);
  const [activeGrade, setActiveGrade] = useState(1);

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

  const filteredLessons = lessons.filter((lesson) => lesson.grade === activeGrade);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Leckék</h1>

      {/* Osztály tab-ok */}
      <div style={{
        display: "flex",
        gap: "0.5rem",
        marginBottom: "1.5rem",
        borderBottom: "2px solid #e5e7eb",
        paddingBottom: "0.5rem"
      }}>
        {[1, 2, 3, 4].map((grade) => (
          <button
            key={grade}
            onClick={() => setActiveGrade(grade)}
            style={{
              padding: "0.75rem 1.5rem",
              fontSize: "1rem",
              fontWeight: activeGrade === grade ? "bold" : "normal",
              cursor: "pointer",
              backgroundColor: activeGrade === grade ? "#3b82f6" : "#f3f4f6",
              color: activeGrade === grade ? "white" : "#374151",
              border: "none",
              borderRadius: "8px 8px 0 0",
              borderBottom: activeGrade === grade ? "3px solid #1d4ed8" : "none",
              transition: "all 0.2s ease"
            }}
          >
            {grade}. Osztály
          </button>
        ))}
      </div>

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
      ) : filteredLessons.length === 0 ? (
        <div style={{
          padding: "2rem",
          textAlign: "center",
          backgroundColor: "#f9fafb",
          borderRadius: "8px",
          color: "#6b7280"
        }}>
          <p style={{ fontSize: "1.2rem" }}>📚 Ebben az osztályban még nincsenek leckék.</p>
          <p>Később új leckék kerülnek ide!</p>
        </div>
      ) : (
        <div style={{ display: "grid", gap: "1rem" }}>
          {filteredLessons.map((lesson) => (
            <div
              key={lesson.id}
              style={{
                border: "1px solid #ddd",
                borderRadius: "8px",
                padding: "1.5rem",
                backgroundColor: "#f0fdf4",
              }}
            >
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "start" }}>
                <div>
                  <h3 style={{ margin: "0 0 0.5rem 0" }}>
                    {lesson.title}
                  </h3>
                  <p style={{ margin: "0 0 0.5rem 0", color: "#666" }}>
                    {lesson.description}
                  </p>
                  <p style={{ margin: 0, fontSize: "0.9rem", color: "#888" }}>
                    🌍 {lesson.language} • 📊 {lesson.level}
                  </p>
                </div>
                <div style={{ display: "flex", gap: "0.5rem", flexDirection: "column" }}>
                  <button
                    onClick={() => onSelectGame && onSelectGame(lesson.id, "vocabulary")}
                    style={{
                      padding: "0.5rem 1rem",
                      fontSize: "0.9rem",
                      cursor: "pointer",
                      backgroundColor: "#4ade80",
                      color: "#fff",
                      border: "none",
                      borderRadius: "6px",
                    }}
                  >
                    📚 Szókincs
                  </button>
                  <button
                    onClick={() => onSelectGame && onSelectGame(lesson.id, "grammar")}
                    style={{
                      padding: "0.5rem 1rem",
                      fontSize: "0.9rem",
                      cursor: "pointer",
                      backgroundColor: "#8b5cf6",
                      color: "#fff",
                      border: "none",
                      borderRadius: "6px",
                    }}
                  >
                    🎓 Nyelvtan
                  </button>
                  <button
                    onClick={() => onSelectGame && onSelectGame(lesson.id, "listening")}
                    style={{
                      padding: "0.5rem 1rem",
                      fontSize: "0.9rem",
                      cursor: "pointer",
                      backgroundColor: "#0891b2",
                      color: "#fff",
                      border: "none",
                      borderRadius: "6px",
                    }}
                  >
                    🎧 Hallgatás
                  </button>
                  <button
                    onClick={() => onSelectGame && onSelectGame(lesson.id, "reading")}
                    style={{
                      padding: "0.5rem 1rem",
                      fontSize: "0.9rem",
                      cursor: "pointer",
                      backgroundColor: "#059669",
                      color: "#fff",
                      border: "none",
                      borderRadius: "6px",
                    }}
                  >
                    📖 Olvasás
                  </button>
                  <button
                    onClick={() => onSelectGame && onSelectGame(lesson.id, "speaking")}
                    style={{
                      padding: "0.5rem 1rem",
                      fontSize: "0.9rem",
                      cursor: "pointer",
                      backgroundColor: "#ec4899",
                      color: "#fff",
                      border: "none",
                      borderRadius: "6px",
                    }}
                  >
                    🎤 Beszéd
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
