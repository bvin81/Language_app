import { useEffect, useState } from "react";
import { getLessons } from "../api/lessonApi";
import { useLanguage } from "../i18n/LanguageContext";

export default function LessonList({ onSelectGame, user }) {
  const [lessons, setLessons] = useState([]);
  const [loading, setLoading] = useState(true);
  const [activeGrade, setActiveGrade] = useState(1);
  const { t } = useLanguage();

  useEffect(() => {
    getLessons()
      .then((data) => { setLessons(data); setLoading(false); })
      .catch(() => setLoading(false));
  }, []);

  if (loading) return <div>{t.loading}</div>;

  const filteredLessons = lessons.filter((lesson) => lesson.grade === activeGrade);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>{t.lessons}</h1>

      <div style={{ display: "flex", gap: "0.5rem", marginBottom: "1.5rem", borderBottom: "2px solid #e5e7eb", paddingBottom: "0.5rem" }}>
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
            {t.grade(grade)}
          </button>
        ))}
      </div>

      <div style={{ marginBottom: "1rem" }}>
        <button onClick={() => window.location.reload()}>{t.refresh}</button>
      </div>

      {lessons.length === 0 ? (
        <div>
          <p>{t.noLessonsDb}</p>
          <p>Run: <code>python -m app.init_db</code></p>
        </div>
      ) : filteredLessons.length === 0 ? (
        <div style={{ padding: "2rem", textAlign: "center", backgroundColor: "#f9fafb", borderRadius: "8px", color: "#6b7280" }}>
          <p style={{ fontSize: "1.2rem" }}>{t.noLessonsGrade}</p>
          <p>{t.noLessonsGradeSub}</p>
        </div>
      ) : (
        <div style={{ display: "grid", gap: "1rem" }}>
          {filteredLessons.map((lesson) => (
            <div
              key={lesson.id}
              style={{ border: "1px solid #ddd", borderRadius: "8px", padding: "1.5rem", backgroundColor: "#f0fdf4" }}
            >
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "start" }}>
                <div>
                  <h3 style={{ margin: "0 0 0.5rem 0" }}>{lesson.title}</h3>
                  <p style={{ margin: "0 0 0.5rem 0", color: "#666" }}>{lesson.description}</p>
                  <p style={{ margin: 0, fontSize: "0.9rem", color: "#888" }}>🌍 {lesson.language} • 📊 {lesson.level}</p>
                </div>
                <div style={{ display: "flex", gap: "0.5rem", flexDirection: "column" }}>
                  {[
                    { key: "vocabulary", label: t.btnVocabulary, color: "#4ade80" },
                    { key: "grammar",    label: t.btnGrammar,    color: "#8b5cf6" },
                    { key: "listening",  label: t.btnListening,  color: "#0891b2" },
                    { key: "reading",    label: t.btnReading,    color: "#059669" },
                    { key: "speaking",   label: t.btnSpeaking,   color: "#ec4899" },
                  ].map(({ key, label, color }) => (
                    <button
                      key={key}
                      onClick={() => onSelectGame && onSelectGame(lesson.id, key)}
                      style={{ padding: "0.5rem 1rem", fontSize: "0.9rem", cursor: "pointer", backgroundColor: color, color: "#fff", border: "none", borderRadius: "6px" }}
                    >
                      {label}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
