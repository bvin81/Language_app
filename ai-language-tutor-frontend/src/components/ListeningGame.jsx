import { useState, useEffect } from "react";

const API_URL = import.meta.env.VITE_API_URL;

export default function ListeningGame({ lessonId, user }) {
  const [gameData, setGameData] = useState(null);
  const [lessonLanguage, setLessonLanguage] = useState("romanian");
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [score, setScore] = useState(0);
  const [showResult, setShowResult] = useState(false);
  const [isFinished, setIsFinished] = useState(false);
  const [isPlaying, setIsPlaying] = useState(false);
  const [showTranscript, setShowTranscript] = useState(false);
  const [playCount, setPlayCount] = useState(0);
  const [playbackSpeed, setPlaybackSpeed] = useState(0.8); // Alapértelmezett lassabb

  useEffect(() => {
    fetchGame();
    fetchLessonInfo();
  }, [lessonId]);

  const fetchLessonInfo = async () => {
    try {
      const res = await fetch(`${API_URL}/lessons/`);
      const lessons = await res.json();
      const lesson = lessons.find(l => l.id === lessonId);
      if (lesson) {
        setLessonLanguage(lesson.language);
      }
    } catch (error) {
      console.error("Hiba a lecke betöltésekor:", error);
    }
  };

  const fetchGame = async () => {
    try {
      const res = await fetch(`${API_URL}/games/listening/${lessonId}`);
      const data = await res.json();

      if (data.error) {
        return;
      }

      setGameData(data.questions);
      setCurrentQuestion(0);
      setScore(0);
      setIsFinished(false);
      setPlayCount(0);
      setShowTranscript(false);
    } catch (error) {
      console.error("Hiba a játék betöltésekor:", error);
    }
  };

  const getLanguageCode = () => {
    switch (lessonLanguage) {
      case "romanian":
        return "ro-RO";
      case "english":
        return "en-US";
      default:
        return "ro-RO";
    }
  };

  const playAudio = () => {
    if (!('speechSynthesis' in window)) {
      alert("A böngésződ nem támogatja a szövegfelolvasást!");
      return;
    }

    // Leállítjuk az előző lejátszást
    speechSynthesis.cancel();

    const question = gameData[currentQuestion];
    const utterance = new SpeechSynthesisUtterance(question.transcript);

    utterance.lang = getLanguageCode();
    utterance.rate = playbackSpeed;
    utterance.pitch = 1;

    utterance.onstart = () => {
      setIsPlaying(true);
    };

    utterance.onend = () => {
      setIsPlaying(false);
    };

    utterance.onerror = () => {
      setIsPlaying(false);
    };

    setPlayCount(prev => prev + 1);
    speechSynthesis.speak(utterance);
  };

  const stopAudio = () => {
    speechSynthesis.cancel();
    setIsPlaying(false);
  };

  const handleAnswer = (answer) => {
    setSelectedAnswer(answer);
    setShowResult(true);
    stopAudio();

    const isCorrect = answer === gameData[currentQuestion].correct_answer;
    if (isCorrect) {
      setScore(score + 1);
    }

    setShowTranscript(true);

    setTimeout(() => {
      setShowResult(false);
      setSelectedAnswer(null);
      setShowTranscript(false);
      setPlayCount(0);

      if (currentQuestion < gameData.length - 1) {
        setCurrentQuestion(currentQuestion + 1);
      } else {
        saveProgress(score + (isCorrect ? 1 : 0), gameData.length);
        setIsFinished(true);
      }
    }, 3000);
  };

  const saveProgress = async (finalScore, total) => {
    try {
      await fetch(`${API_URL}/progress/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          user_id: user.id,
          lesson_id: lessonId,
          score: finalScore,
          total: total
        })
      });
    } catch (error) {
      console.error("Hiba az eredmény mentésekor:", error);
    }
  };

  const getDifficultyStars = (difficulty) => {
    return "⭐".repeat(difficulty);
  };

  const getSpeedLabel = () => {
    if (playbackSpeed <= 0.5) return "Nagyon lassú";
    if (playbackSpeed <= 0.7) return "Lassú";
    if (playbackSpeed <= 0.9) return "Normál";
    if (playbackSpeed <= 1.1) return "Gyors";
    return "Nagyon gyors";
  };

  if (!gameData || gameData.length === 0) {
    return (
      <div style={{ textAlign: "center", padding: "2rem" }}>
        <h2>Hallásértés gyakorlatok</h2>
        <p>Ehhez a leckéhez még nincsenek hallásértés gyakorlatok.</p>
        <p style={{ color: "#666", fontSize: "0.9rem" }}>
          Próbáld ki a szókincsjátékot vagy a nyelvtan gyakorlatokat!
        </p>
      </div>
    );
  }

  if (isFinished) {
    const percentage = Math.round((score / gameData.length) * 100);
    return (
      <div style={{ textAlign: "center", padding: "2rem" }}>
        <h2>🎧 Hallásértés vége!</h2>
        <p style={{ fontSize: "2rem" }}>
          Eredmény: {score} / {gameData.length}
        </p>
        <p style={{
          fontSize: "1.5rem",
          color: percentage >= 80 ? "#16a34a" : percentage >= 50 ? "#ea580c" : "#dc2626"
        }}>
          {percentage}%
        </p>
        <p style={{ marginTop: "1rem", color: "#666" }}>
          {percentage >= 80 ? "Kiváló hallás! 🌟" :
           percentage >= 50 ? "Jó munka! Gyakorolj tovább a hallgatással!" :
           "Ne add fel! Hallgasd többször!"}
        </p>
        <button
          onClick={fetchGame}
          style={{
            marginTop: "1rem",
            padding: "0.75rem 1.5rem",
            cursor: "pointer",
            backgroundColor: "#0891b2",
            color: "white",
            border: "none",
            borderRadius: "8px",
            fontSize: "1rem"
          }}
        >
          Újra próbálom
        </button>
      </div>
    );
  }

  const question = gameData[currentQuestion];

  return (
    <div style={{ maxWidth: "600px", margin: "0 auto", padding: "2rem" }}>
      {/* Fejléc */}
      <div style={{
        marginBottom: "2rem",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center"
      }}>
        <div>
          <p style={{ fontSize: "0.9rem", color: "#666", margin: 0 }}>
            Kérdés {currentQuestion + 1} / {gameData.length}
          </p>
          <p style={{ fontSize: "0.9rem", color: "#666", margin: 0 }}>
            Pontszám: {score}
          </p>
        </div>
        <div style={{
          backgroundColor: "#e0f2fe",
          padding: "0.5rem 1rem",
          borderRadius: "20px",
          fontSize: "0.85rem",
          color: "#0369a1"
        }}>
          {getDifficultyStars(question.difficulty)} {lessonLanguage === "romanian" ? "Román" : "Angol"}
        </div>
      </div>

      {/* Audio lejátszó */}
      <div style={{
        marginBottom: "2rem",
        padding: "1.5rem",
        backgroundColor: "#f0f9ff",
        borderRadius: "12px",
        border: "2px solid #bae6fd",
        textAlign: "center"
      }}>
        {/* Lejátszás gomb */}
        <button
          onClick={isPlaying ? stopAudio : playAudio}
          disabled={showResult}
          style={{
            padding: "1rem 2rem",
            fontSize: "1.2rem",
            cursor: showResult ? "default" : "pointer",
            backgroundColor: showResult ? "#94a3b8" : isPlaying ? "#ef4444" : "#0891b2",
            color: "white",
            border: "none",
            borderRadius: "50px",
            display: "flex",
            alignItems: "center",
            gap: "0.5rem",
            margin: "0 auto"
          }}
        >
          {isPlaying ? (
            <>⏹️ Megállítás</>
          ) : (
            <>▶️ Hallgatás</>
          )}
        </button>

        <p style={{ marginTop: "1rem", fontSize: "0.85rem", color: "#64748b" }}>
          Lejátszások száma: {playCount}
        </p>

        {/* Sebesség csúszka */}
        <div style={{
          marginTop: "1.5rem",
          padding: "1rem",
          backgroundColor: "#e0f2fe",
          borderRadius: "10px"
        }}>
          <label style={{
            display: "block",
            marginBottom: "0.5rem",
            fontSize: "0.9rem",
            color: "#0369a1",
            fontWeight: "bold"
          }}>
            🎚️ Lejátszási sebesség: {getSpeedLabel()} ({playbackSpeed.toFixed(1)}x)
          </label>
          <input
            type="range"
            min="0.3"
            max="1.5"
            step="0.1"
            value={playbackSpeed}
            onChange={(e) => setPlaybackSpeed(parseFloat(e.target.value))}
            disabled={isPlaying}
            style={{
              width: "100%",
              height: "8px",
              cursor: isPlaying ? "default" : "pointer",
              accentColor: "#0891b2"
            }}
          />
          <div style={{
            display: "flex",
            justifyContent: "space-between",
            fontSize: "0.75rem",
            color: "#64748b",
            marginTop: "0.25rem"
          }}>
            <span>Lassú</span>
            <span>Normál</span>
            <span>Gyors</span>
          </div>
        </div>

        {/* Transcript megjelenítés válasz után */}
        {showTranscript && question.transcript && (
          <div style={{
            marginTop: "1rem",
            padding: "1rem",
            backgroundColor: "#fef3c7",
            borderRadius: "8px",
            border: "1px solid #fcd34d"
          }}>
            <p style={{ margin: 0, fontStyle: "italic", color: "#92400e" }}>
              📝 "{question.transcript}"
            </p>
          </div>
        )}
      </div>

      {/* Kérdés */}
      <div style={{
        marginBottom: "1.5rem",
        textAlign: "center"
      }}>
        <h2 style={{
          fontSize: "1.3rem",
          color: "#0c4a6e"
        }}>
          {question.question}
        </h2>
      </div>

      {/* Válaszlehetőségek */}
      <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
        {question.options.map((option, index) => {
          let buttonStyle = {
            padding: "1rem",
            fontSize: "1.1rem",
            cursor: showResult ? "default" : "pointer",
            border: "2px solid #bae6fd",
            borderRadius: "8px",
            backgroundColor: "#fff",
            transition: "all 0.2s",
          };

          if (showResult) {
            if (option === question.correct_answer) {
              buttonStyle.backgroundColor = "#4ade80";
              buttonStyle.borderColor = "#22c55e";
              buttonStyle.color = "#fff";
            } else if (option === selectedAnswer) {
              buttonStyle.backgroundColor = "#f87171";
              buttonStyle.borderColor = "#ef4444";
              buttonStyle.color = "#fff";
            }
          }

          return (
            <button
              key={index}
              onClick={() => !showResult && handleAnswer(option)}
              style={buttonStyle}
              disabled={showResult}
            >
              {option}
            </button>
          );
        })}
      </div>

      {/* Eredmény */}
      {showResult && (
        <div
          style={{
            marginTop: "2rem",
            padding: "1rem",
            borderRadius: "8px",
            backgroundColor: selectedAnswer === question.correct_answer ? "#dcfce7" : "#fee2e2",
            textAlign: "center",
          }}
        >
          {selectedAnswer === question.correct_answer ? (
            <p style={{ color: "#16a34a", fontWeight: "bold", margin: 0 }}>
              ✓ Helyes!
            </p>
          ) : (
            <p style={{ color: "#dc2626", fontWeight: "bold", margin: 0 }}>
              ✗ Helyes válasz: {question.correct_answer}
            </p>
          )}
        </div>
      )}
    </div>
  );
}
