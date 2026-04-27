import { useState, useEffect } from "react";
import { useLanguage } from "../i18n/LanguageContext";

const API_URL = import.meta.env.VITE_API_URL;

export default function ReadingGame({ lessonId, user }) {
  const [readingsData, setReadingsData] = useState(null);
  const [currentReading, setCurrentReading] = useState(0);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [score, setScore] = useState(0);
  const [showResult, setShowResult] = useState(false);
  const [isFinished, setIsFinished] = useState(false);
  const [showQuestions, setShowQuestions] = useState(false);
  const [totalQuestions, setTotalQuestions] = useState(0);
  const { t } = useLanguage();

  useEffect(() => { fetchGame(); }, [lessonId]);

  const fetchGame = async () => {
    try {
      const res = await fetch(`${API_URL}/games/reading/${lessonId}`);
      const data = await res.json();
      if (data.error) { alert(data.error); return; }
      setReadingsData(data.readings);
      setCurrentReading(0);
      setCurrentQuestion(0);
      setScore(0);
      setIsFinished(false);
      setShowQuestions(false);
      const total = data.readings.reduce((sum, r) => sum + r.questions.length, 0);
      setTotalQuestions(total);
    } catch (error) {
      console.error("Error loading game:", error);
    }
  };

  const handleAnswer = (answer) => {
    setSelectedAnswer(answer);
    setShowResult(true);
    const reading = readingsData[currentReading];
    const question = reading.questions[currentQuestion];
    const isCorrect = answer === question.correct_answer;
    if (isCorrect) setScore(score + 1);
    setTimeout(() => {
      setShowResult(false);
      setSelectedAnswer(null);
      if (currentQuestion < reading.questions.length - 1) {
        setCurrentQuestion(currentQuestion + 1);
      } else if (currentReading < readingsData.length - 1) {
        setCurrentReading(currentReading + 1);
        setCurrentQuestion(0);
        setShowQuestions(false);
      } else {
        saveProgress(score + (isCorrect ? 1 : 0), totalQuestions);
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

  const getDifficultyStars = (difficulty) => "⭐".repeat(difficulty);

  if (!readingsData || readingsData.length === 0) {
    return (
      <div style={{ textAlign: "center", padding: "2rem" }}>
        <h2>📖</h2>
        <p>{t.noReading}</p>
        <p style={{ color: "#666", fontSize: "0.9rem" }}>{t.noReadingSub}</p>
      </div>
    );
  }

  if (isFinished) {
    const percentage = Math.round((score / totalQuestions) * 100);
    return (
      <div style={{ textAlign: "center", padding: "2rem" }}>
        <h2>{t.readingGameOver}</h2>
        <p style={{ fontSize: "2rem" }}>{t.result(score, totalQuestions)}</p>
        <p style={{ fontSize: "1.5rem", color: percentage >= 80 ? "#16a34a" : percentage >= 50 ? "#ea580c" : "#dc2626" }}>{percentage}%</p>
        <p style={{ marginTop: "1rem", color: "#666" }}>
          {percentage >= 80 ? t.readingExcellent : percentage >= 50 ? t.readingGood : t.readingKeepGoing}
        </p>
        <button onClick={fetchGame} style={{ marginTop: "1rem", padding: "0.75rem 1.5rem", cursor: "pointer", backgroundColor: "#059669", color: "white", border: "none", borderRadius: "8px", fontSize: "1rem" }}>
          {t.tryAgain}
        </button>
      </div>
    );
  }

  const reading = readingsData[currentReading];

  if (!showQuestions) {
    return (
      <div style={{ maxWidth: "700px", margin: "0 auto", padding: "2rem" }}>
        <div style={{ marginBottom: "1.5rem", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <p style={{ fontSize: "0.9rem", color: "#666", margin: 0 }}>{t.textOf(currentReading + 1, readingsData.length)}</p>
          <div style={{ backgroundColor: "#d1fae5", padding: "0.5rem 1rem", borderRadius: "20px", fontSize: "0.85rem", color: "#047857" }}>
            {getDifficultyStars(reading.difficulty)} {t.readingLabel}
          </div>
        </div>

        <h2 style={{ fontSize: "1.5rem", color: "#065f46", marginBottom: "1rem", textAlign: "center" }}>📖 {reading.title}</h2>

        <div style={{ padding: "1.5rem", backgroundColor: "#f0fdf4", borderRadius: "12px", border: "2px solid #a7f3d0", marginBottom: "2rem", lineHeight: "1.8", fontSize: "1.1rem" }}>
          {reading.content.split('\n').map((paragraph, idx) => (
            <p key={idx} style={{ marginBottom: "1rem" }}>{paragraph}</p>
          ))}
        </div>

        <div style={{ textAlign: "center" }}>
          <p style={{ color: "#666", marginBottom: "1rem" }}>{t.readingInstruction}</p>
          <button onClick={() => setShowQuestions(true)} style={{ padding: "1rem 2rem", fontSize: "1.1rem", cursor: "pointer", backgroundColor: "#059669", color: "white", border: "none", borderRadius: "8px" }}>
            {t.answerQuestions}
          </button>
        </div>
      </div>
    );
  }

  const question = reading.questions[currentQuestion];

  return (
    <div style={{ maxWidth: "600px", margin: "0 auto", padding: "2rem" }}>
      <div style={{ marginBottom: "2rem", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div>
          <p style={{ fontSize: "0.9rem", color: "#666", margin: 0 }}>{t.questionOf(currentQuestion + 1, reading.questions.length)}</p>
          <p style={{ fontSize: "0.9rem", color: "#666", margin: 0 }}>{t.score} {score}</p>
        </div>
        <div style={{ backgroundColor: "#d1fae5", padding: "0.5rem 1rem", borderRadius: "20px", fontSize: "0.85rem", color: "#047857" }}>
          📖 {reading.title}
        </div>
      </div>

      <div style={{ marginBottom: "2rem", padding: "1.5rem", backgroundColor: "#ecfdf5", borderRadius: "12px", border: "2px solid #a7f3d0" }}>
        <h2 style={{ fontSize: "1.3rem", color: "#065f46", margin: 0 }}>{question.question}</h2>
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
        {question.options.map((option, index) => {
          let buttonStyle = { padding: "1rem", fontSize: "1.1rem", cursor: showResult ? "default" : "pointer", border: "2px solid #a7f3d0", borderRadius: "8px", backgroundColor: "#fff", transition: "all 0.2s" };
          if (showResult) {
            if (option === question.correct_answer) { buttonStyle.backgroundColor = "#4ade80"; buttonStyle.borderColor = "#22c55e"; buttonStyle.color = "#fff"; }
            else if (option === selectedAnswer) { buttonStyle.backgroundColor = "#f87171"; buttonStyle.borderColor = "#ef4444"; buttonStyle.color = "#fff"; }
          }
          return (
            <button key={index} onClick={() => !showResult && handleAnswer(option)} style={buttonStyle} disabled={showResult}>{option}</button>
          );
        })}
      </div>

      {showResult && (
        <div style={{ marginTop: "2rem", padding: "1rem", borderRadius: "8px", backgroundColor: selectedAnswer === question.correct_answer ? "#dcfce7" : "#fee2e2", textAlign: "center" }}>
          {selectedAnswer === question.correct_answer
            ? <p style={{ color: "#16a34a", fontWeight: "bold", margin: 0 }}>{t.correct}</p>
            : <p style={{ color: "#dc2626", fontWeight: "bold", margin: 0 }}>{t.wrongAnswer(question.correct_answer)}</p>
          }
        </div>
      )}
    </div>
  );
}
