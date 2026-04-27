import { useState, useEffect } from "react";
import { useLanguage } from "../i18n/LanguageContext";

const API_URL = import.meta.env.VITE_API_URL;

export default function GrammarGame({ lessonId, user }) {
  const [gameData, setGameData] = useState(null);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [score, setScore] = useState(0);
  const [showResult, setShowResult] = useState(false);
  const [isFinished, setIsFinished] = useState(false);
  const [showExplanation, setShowExplanation] = useState(false);
  const { t } = useLanguage();

  useEffect(() => { fetchGame(); }, [lessonId]);

  const fetchGame = async () => {
    try {
      const res = await fetch(`${API_URL}/games/grammar/${lessonId}`);
      const data = await res.json();
      if (data.error) { alert(data.error); return; }
      setGameData(data.questions);
      setCurrentQuestion(0);
      setScore(0);
      setIsFinished(false);
      setShowExplanation(false);
    } catch (error) {
      console.error("Error loading game:", error);
    }
  };

  const handleAnswer = (answer) => {
    setSelectedAnswer(answer);
    setShowResult(true);
    const isCorrect = answer === gameData[currentQuestion].correct_answer;
    if (isCorrect) setScore(score + 1);
    setShowExplanation(true);
    setTimeout(() => {
      setShowResult(false);
      setSelectedAnswer(null);
      setShowExplanation(false);
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
        body: JSON.stringify({ user_id: user.id, lesson_id: lessonId, score: finalScore, total })
      });
    } catch (error) {
      console.error("Error saving progress:", error);
    }
  };

  const getExerciseTypeLabel = (type) => {
    switch (type) {
      case "fill_blank": return t.fillBlank;
      case "multiple_choice": return t.multipleChoice;
      case "word_order": return t.wordOrder;
      default: return t.exerciseDefault;
    }
  };

  const getDifficultyStars = (difficulty) => "⭐".repeat(difficulty);

  if (!gameData || gameData.length === 0) {
    return (
      <div style={{ textAlign: "center", padding: "2rem" }}>
        <h2>{t.exerciseDefault}</h2>
        <p>{t.noGrammar}</p>
        <p style={{ color: "#666", fontSize: "0.9rem" }}>{t.noGrammarSub}</p>
      </div>
    );
  }

  if (isFinished) {
    const percentage = Math.round((score / gameData.length) * 100);
    return (
      <div style={{ textAlign: "center", padding: "2rem" }}>
        <h2>{t.grammarGameOver}</h2>
        <p style={{ fontSize: "2rem" }}>{t.result(score, gameData.length)}</p>
        <p style={{ fontSize: "1.5rem", color: percentage >= 80 ? "#16a34a" : percentage >= 50 ? "#ea580c" : "#dc2626" }}>{percentage}%</p>
        <p style={{ marginTop: "1rem", color: "#666" }}>
          {percentage >= 80 ? t.grammarExcellent : percentage >= 50 ? t.grammarGood : t.grammarKeepGoing}
        </p>
        <button onClick={fetchGame} style={{ marginTop: "1rem", padding: "0.75rem 1.5rem", cursor: "pointer", backgroundColor: "#8b5cf6", color: "white", border: "none", borderRadius: "8px", fontSize: "1rem" }}>
          {t.tryAgain}
        </button>
      </div>
    );
  }

  const question = gameData[currentQuestion];

  return (
    <div style={{ maxWidth: "600px", margin: "0 auto", padding: "2rem" }}>
      <div style={{ marginBottom: "2rem", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div>
          <p style={{ fontSize: "0.9rem", color: "#666", margin: 0 }}>{t.questionOf(currentQuestion + 1, gameData.length)}</p>
          <p style={{ fontSize: "0.9rem", color: "#666", margin: 0 }}>{t.score} {score}</p>
        </div>
        <div style={{ backgroundColor: "#f3e8ff", padding: "0.5rem 1rem", borderRadius: "20px", fontSize: "0.85rem", color: "#7c3aed" }}>
          {getDifficultyStars(question.difficulty)} {getExerciseTypeLabel(question.exercise_type)}
        </div>
      </div>

      <div style={{ marginBottom: "2rem", padding: "1.5rem", backgroundColor: "#faf5ff", borderRadius: "12px", border: "2px solid #e9d5ff" }}>
        <h2 style={{ fontSize: "1.5rem", marginBottom: "0.5rem", color: "#581c87" }}>{question.question}</h2>
        {question.exercise_type === "word_order" && (
          <p style={{ fontSize: "0.85rem", color: "#7c3aed", marginTop: "0.5rem" }}>{t.wordOrderTip}</p>
        )}
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
        {question.options.map((option, index) => {
          let buttonStyle = {
            padding: "1rem", fontSize: "1.1rem",
            cursor: showResult ? "default" : "pointer",
            border: "2px solid #e9d5ff", borderRadius: "8px",
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
        <div style={{ marginTop: "2rem" }}>
          <div style={{ padding: "1rem", borderRadius: "8px", backgroundColor: selectedAnswer === question.correct_answer ? "#dcfce7" : "#fee2e2", textAlign: "center", marginBottom: "1rem" }}>
            {selectedAnswer === question.correct_answer
              ? <p style={{ color: "#16a34a", fontWeight: "bold", margin: 0 }}>{t.correct}</p>
              : <p style={{ color: "#dc2626", fontWeight: "bold", margin: 0 }}>{t.wrongAnswer(question.correct_answer)}</p>
            }
          </div>
          {showExplanation && question.explanation && (
            <div style={{ padding: "1rem", backgroundColor: "#fef3c7", borderRadius: "8px", border: "1px solid #fcd34d" }}>
              <p style={{ margin: 0, color: "#92400e" }}>
                <strong>{t.explanation}</strong> {question.explanation}
              </p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
