import { useState, useEffect } from "react";
import Login from "./components/Login";
import LessonList from "./pages/LessonList";
import Statistics from "./pages/Statistics";
import VocabularyGame from "./components/VocabularyGame";
import GrammarGame from "./components/GrammarGame";
import ListeningGame from "./components/ListeningGame";
import ReadingGame from "./components/ReadingGame";
import SpeakingGame from "./components/SpeakingGame";
import { useLanguage } from "./i18n/LanguageContext";

function App() {
  const [user, setUser] = useState(null);
  const [selectedLesson, setSelectedLesson] = useState(null);
  const [selectedGameType, setSelectedGameType] = useState(null);
  const [currentPage, setCurrentPage] = useState("lessons");
  const { t, lang, toggle } = useLanguage();

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

  const langToggleBtn = (
    <button
      onClick={toggle}
      style={{
        padding: "0.4rem 0.9rem",
        backgroundColor: lang === "en" ? "#1d4ed8" : "#6b7280",
        color: "white",
        border: "none",
        borderRadius: "6px",
        cursor: "pointer",
        fontWeight: "bold",
        fontSize: "0.85rem",
        letterSpacing: "0.05em"
      }}
      title={lang === "hu" ? "Switch to English" : "Váltás magyarra"}
    >
      {lang === "hu" ? "EN" : "HU"}
    </button>
  );

  if (selectedLesson && selectedGameType) {
    return (
      <div>
        <div style={{ display: "flex", alignItems: "center", gap: "1rem", margin: "1rem" }}>
          <button
            onClick={handleBackToLessons}
            style={{
              padding: "0.5rem 1rem",
              cursor: "pointer",
              backgroundColor: "#3b82f6",
              color: "white",
              border: "none",
              borderRadius: "8px"
            }}
          >
            {t.backToLessons}
          </button>
          {langToggleBtn}
        </div>
        {selectedGameType === "vocabulary" && <VocabularyGame lessonId={selectedLesson} user={user} />}
        {selectedGameType === "grammar" && <GrammarGame lessonId={selectedLesson} user={user} />}
        {selectedGameType === "listening" && <ListeningGame lessonId={selectedLesson} user={user} />}
        {selectedGameType === "reading" && <ReadingGame lessonId={selectedLesson} user={user} />}
        {selectedGameType === "speaking" && <SpeakingGame lessonId={selectedLesson} user={user} />}
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
            {t.navLessons}
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
            {t.navStatistics}
          </button>
        </div>

        <div style={{ display: "flex", gap: "1rem", alignItems: "center" }}>
          {langToggleBtn}
          <span>{t.loggedIn} <strong>{user.name}</strong></span>
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
            {t.logout}
          </button>
        </div>
      </div>

      {currentPage === "lessons" && <LessonList onSelectGame={handleSelectGame} user={user} />}
      {currentPage === "statistics" && <Statistics user={user} />}
    </div>
  );
}

export default App;
