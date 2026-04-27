import { useState, useEffect } from "react";
import { useLanguage } from "../i18n/LanguageContext";

const API_URL = import.meta.env.VITE_API_URL;

export default function VocabularyGame({ lessonId, user }) {
  const [gameData, setGameData] = useState(null);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [score, setScore] = useState(0);
  const [showResult, setShowResult] = useState(false);
  const [isFinished, setIsFinished] = useState(false);
  const { t } = useLanguage();

  useEffect(() => { fetchGame(); }, [lessonId]);

  const fetchGame = async () => {
    try {
      const res = await fetch(`${API_URL}/games/vocabulary/${lessonId}`);
      const data = await res.json();
      if (data.error) { alert(data.error); return; }
      setGameData(data.questions);
      setCurrentQuestion(0);
      setScore(0);
      setIsFinished(false);
    } catch (error) {
      console.error("Error loading game:", error);
    }
  };

  const handleAnswer = (answer) => {
    setSelectedAnswer(answer);
    setShowResult(true);
    const isCorrect = answer === gameData[currentQuestion].correct_answer;
    if (isCorrect) setScore(score + 1);
    setTimeout(() => {
      setShowResult(false);
      setSelectedAnswer(null);
      if (currentQuestion < gameData.length - 1) {
        setCurrentQuestion(currentQuestion + 1);
      } else {
        saveProgress(score + (isCorrect ? 1 : 0), gameData.length);
        setIsFinished(true);
      }
    }, 2000);
  };

  const saveProgress = async (finalScore, total) => {
    try {
      await fetch(`${API_URL}/progress/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: user.id, lesson_id: lessonId, score: finalScore, total })
      });
    } catch (error) {
      console.error("Error saving progress:", error);
    }
  };

  if (!gameData) return <div>{t.loading}</div>;

  if (isFinished) {
    const percentage = Math.round((score / gameData.length) * 100);
    return (
      <div style={{ textAlign: "center", padding: "2rem" }}>
        <h2>{t.vocabGameOver}</h2>
        <p style={{ fontSize: "2rem" }}>{t.result(score, gameData.length)}</p>
        <p style={{ fontSize: "1.5rem", color: percentage >= 80 ? "#16a34a" : "#ea580c" }}>{percentage}%</p>
        <button onClick={fetchGame} style={{ marginTop: "1rem", padding: "0.5rem 1rem", cursor: "pointer" }}>
          {t.playAgain}
        </button>
      </div>
    );
  }

  const question = gameData[currentQuestion];

  return (
    <div style={{ maxWidth: "600px", margin: "0 auto", padding: "2rem" }}>
      <div style={{ marginBottom: "2rem" }}>
        <p style={{ fontSize: "0.9rem", color: "#666" }}>{t.questionOf(currentQuestion + 1, gameData.length)}</p>
        <p style={{ fontSize: "0.9rem", color: "#666" }}>{t.score} {score}</p>
      </div>

      <div style={{ marginBottom: "2rem" }}>
        <h2 style={{ fontSize: "2rem", marginBottom: "1rem" }}>{question.question}</h2>
        {question.example && (
          <p style={{ fontStyle: "italic", color: "#555", fontSize: "0.9rem" }}>{question.example}</p>
        )}
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
        {question.options.map((option, index) => {
          let buttonStyle = {
            padding: "1rem", fontSize: "1.1rem",
            cursor: showResult ? "default" : "pointer",
            border: "2px solid #ddd", borderRadius: "8px",
            backgroundColor: "#fff", transition: "all 0.2s",
          };
          if (showResult) {
            if (option === question.correct_answer) { buttonStyle.backgroundColor = "#4ade80"; buttonStyle.borderColor = "#22c55e"; buttonStyle.color = "#fff"; }
            else if (option === selectedAnswer) { buttonStyle.backgroundColor = "#f87171"; buttonStyle.borderColor = "#ef4444"; buttonStyle.color = "#fff"; }
          }
          return (
            <button key={index} onClick={() => !showResult && handleAnswer(option)} style={buttonStyle} disabled={showResult}>
              {option}
            </button>
          );
        })}
      </div>

      {showResult && (
        <div style={{ marginTop: "2rem", padding: "1rem", borderRadius: "8px", backgroundColor: selectedAnswer === question.correct_answer ? "#dcfce7" : "#fee2e2", textAlign: "center" }}>
          {selectedAnswer === question.correct_answer
            ? <p style={{ color: "#16a34a", fontWeight: "bold" }}>{t.correct}</p>
            : <p style={{ color: "#dc2626", fontWeight: "bold" }}>{t.wrongAnswer(question.correct_answer)}</p>
          }
        </div>
      )}
    </div>
  );
}
