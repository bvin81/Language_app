import { useState, useEffect } from "react";
import Login from "./components/Login";
import LessonList from "./pages/LessonList";
import Statistics from "./pages/Statistics";
import VocabularyGame from "./components/VocabularyGame";
import PremiumButton from "./components/PremiumButton";

function App() {
  const [user, setUser] = useState(null);
  const [selectedLesson, setSelectedLesson] = useState(null);
  const [currentPage, setCurrentPage] = useState("lessons"); // új

  useEffect(() => {
    const savedUser = localStorage.getItem("user");
    if (savedUser) {
      setUser(JSON.parse(savedUser));
    }
  }, []);

  if (!user) {
    return <Login onLogin={setUser} />;
  }

  if (selectedLesson) {
    return (
      <div>
        <button
          onClick={() => setSelectedLesson(null)}
          style={{
            margin: "1rem",
            padding: "0.5rem 1rem",
            cursor: "pointer",
            backgroundColor: "#3b82f6",
            color: "white",
            border: "none",
            borderRadius: "8px"
          }}
        >
          ← Vissza a leckékhez
        </button>
        <VocabularyGame lessonId={selectedLesson} user={user} />
      </div>
    );
  }

  return (
    <div>
      <div style={{
        padding: "1rem",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        borderBottom: "1px solid #ddd"
      }}>
        <div style={{ display: "flex", gap: "1rem", alignItems: "center" }}>
          <button
            onClick={() => setCurrentPage("lessons")}
            style={{
              padding: "0.5rem 1rem",
              backgroundColor: currentPage === "lessons" ? "#3b82f6" : "#e5e7eb",
              color: currentPage === "lessons" ? "white" : "black",
              border: "none",
              borderRadius: "8px",
              cursor: "pointer"
            }}
          >
            📚 Leckék
          </button>
          <button
            onClick={() => setCurrentPage("statistics")}
            style={{
              padding: "0.5rem 1rem",
              backgroundColor: currentPage === "statistics" ? "#3b82f6" : "#e5e7eb",
              color: currentPage === "statistics" ? "white" : "black",
              border: "none",
              borderRadius: "8px",
              cursor: "pointer"
            }}
          >
            📊 Statisztika
          </button>
        </div>

        <div>
          Bejelentkezve: <strong>{user.name}</strong> {user.is_premium && "👑"}
        </div>

        <div style={{ display: "flex", gap: "1rem", alignItems: "center" }}>
          <PremiumButton user={user} onUpgrade={setUser} />
          <button
            onClick={() => {
              localStorage.removeItem("user");
              setUser(null);
            }}
            style={{
              padding: "0.5rem 1rem",
              backgroundColor: "#ef4444",
              color: "white",
              border: "none",
              borderRadius: "8px",
              cursor: "pointer"
            }}
          >
            Kijelentkezés
          </button>
        </div>
      </div>

      {currentPage === "lessons" && (
        <LessonList onSelectLesson={setSelectedLesson} user={user} />
      )}

      {currentPage === "statistics" && (
        <Statistics user={user} />
      )}
    </div>
  );
}

export default App;