import { useState, useEffect } from "react";
import Login from "./components/Login";
import LessonList from "./pages/LessonList";
import Statistics from "./pages/Statistics";
import VocabularyGame from "./components/VocabularyGame";
import GrammarGame from "./components/GrammarGame";
import ListeningGame from "./components/ListeningGame";
import ReadingGame from "./components/ReadingGame";
import SpeakingGame from "./components/SpeakingGame";

function App() {
  const [user, setUser] = useState(null);
  const [selectedLesson, setSelectedLesson] = useState(null);
  const [selectedGameType, setSelectedGameType] = useState(null); // "vocabulary" vagy "grammar"
  const [currentPage, setCurrentPage] = useState("lessons");

  useEffect(() => {
    const savedUser = localStorage.getItem("user");
    if (savedUser) {
      setUser(JSON.parse(savedUser));
    }
  }, []);

  if (!user) {
    return <Login onLogin={setUser} />;
  }

  const handleBackToLessons = () => {
    setSelectedLesson(null);
    setSelectedGameType(null);
  };

  const handleSelectGame = (lessonId, gameType) => {
    setSelectedLesson(lessonId);
    setSelectedGameType(gameType);
  };

  if (selectedLesson && selectedGameType) {
    return (
      <div>
        <button
          onClick={handleBackToLessons}
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
        {selectedGameType === "vocabulary" && (
          <VocabularyGame lessonId={selectedLesson} user={user} />
        )}
        {selectedGameType === "grammar" && (
          <GrammarGame lessonId={selectedLesson} user={user} />
        )}
        {selectedGameType === "listening" && (
          <ListeningGame lessonId={selectedLesson} user={user} />
        )}
        {selectedGameType === "reading" && (
          <ReadingGame lessonId={selectedLesson} user={user} />
        )}
        {selectedGameType === "speaking" && (
          <SpeakingGame lessonId={selectedLesson} user={user} />
        )}
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
          Bejelentkezve: <strong>{user.name}</strong>
        </div>

        <div style={{ display: "flex", gap: "1rem", alignItems: "center" }}>
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
        <LessonList onSelectGame={handleSelectGame} user={user} />
      )}

      {currentPage === "statistics" && (
        <Statistics user={user} />
      )}
    </div>
  );
}

export default App;