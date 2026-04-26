import { useState, useEffect } from "react";

const API_URL = import.meta.env.VITE_API_URL;

export default function AdminPanel({ user }) {
  const [lessons, setLessons] = useState([]);
  const [newLesson, setNewLesson] = useState({
    title: "",
    description: "",
    language: "romanian",
    level: "beginner",
    grade: 1,
    order: 0
  });

  useEffect(() => {
    fetchLessons();
  }, []);

  const fetchLessons = async () => {
    const res = await fetch(`${API_URL}/lessons/`);
    const data = await res.json();
    setLessons(data);
  };

  const handleCreate = async (e) => {
    e.preventDefault();

    await fetch(`${API_URL}/admin/lessons?user_id=${user.id}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newLesson)
    });

    setNewLesson({
      title: "",
      description: "",
      language: "romanian",
      level: "beginner",
      grade: 1,
      order: 0
    });

    fetchLessons();
  };

  const handleDelete = async (lessonId) => {
    if (!confirm("Biztosan törlöd ezt a leckét?")) return;

    await fetch(`${API_URL}/admin/lessons/${lessonId}?user_id=${user.id}`, {
      method: "DELETE"
    });

    fetchLessons();
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "1000px", margin: "0 auto" }}>
      <h1>⚙️ Admin Panel</h1>

      <div style={{
        padding: "2rem",
        backgroundColor: "#f9fafb",
        borderRadius: "8px",
        marginBottom: "2rem"
      }}>
        <h2>Új lecke létrehozása</h2>
        <form onSubmit={handleCreate} style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
          <input
            type="text"
            placeholder="Cím"
            value={newLesson.title}
            onChange={(e) => setNewLesson({...newLesson, title: e.target.value})}
            required
            style={{ padding: "0.5rem", border: "1px solid #ddd", borderRadius: "4px" }}
          />
          <input
            type="text"
            placeholder="Leírás"
            value={newLesson.description}
            onChange={(e) => setNewLesson({...newLesson, description: e.target.value})}
            style={{ padding: "0.5rem", border: "1px solid #ddd", borderRadius: "4px" }}
          />
          <select
            value={newLesson.language}
            onChange={(e) => setNewLesson({...newLesson, language: e.target.value})}
            style={{ padding: "0.5rem", border: "1px solid #ddd", borderRadius: "4px" }}
          >
            <option value="romanian">Román</option>
            <option value="english">Angol</option>
          </select>
          <select
            value={newLesson.level}
            onChange={(e) => setNewLesson({...newLesson, level: e.target.value})}
            style={{ padding: "0.5rem", border: "1px solid #ddd", borderRadius: "4px" }}
          >
            <option value="beginner">Beginner</option>
            <option value="intermediate">Intermediate</option>
            <option value="advanced">Advanced</option>
          </select>
          <select
            value={newLesson.grade}
            onChange={(e) => setNewLesson({...newLesson, grade: parseInt(e.target.value)})}
            style={{ padding: "0.5rem", border: "1px solid #ddd", borderRadius: "4px" }}
          >
            <option value={1}>1. Osztály</option>
            <option value={2}>2. Osztály</option>
            <option value={3}>3. Osztály</option>
            <option value={4}>4. Osztály</option>
          </select>
          <button
            type="submit"
            style={{
              padding: "0.75rem",
              backgroundColor: "#3b82f6",
              color: "white",
              border: "none",
              borderRadius: "8px",
              cursor: "pointer",
              fontWeight: "bold"
            }}
          >
            Lecke létrehozása
          </button>
        </form>
      </div>

      <h2>Leckék kezelése</h2>
      <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
        {lessons.map((lesson) => (
          <div
            key={lesson.id}
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
              <strong>{lesson.title}</strong>
              <span style={{ marginLeft: "0.5rem", color: "#3b82f6", fontSize: "0.8rem" }}>
                {lesson.grade}. osztály
              </span>
              <div style={{ fontSize: "0.9rem", color: "#666" }}>
                {lesson.language} • {lesson.level}
              </div>
            </div>
            <button
              onClick={() => handleDelete(lesson.id)}
              style={{
                padding: "0.5rem 1rem",
                backgroundColor: "#ef4444",
                color: "white",
                border: "none",
                borderRadius: "4px",
                cursor: "pointer"
              }}
            >
              Törlés
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}