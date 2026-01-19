import { useState, useEffect } from "react";

const API_URL = import.meta.env.VITE_API_URL;

export default function VocabularyGame({ lessonId }) {
  const [gameData, setGameData] = useState(null);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [score, setScore] = useState(0);
  const [showResult, setShowResult] = useState(false);
  const [isFinished, setIsFinished] = useState(false);

  useEffect(() => {
    fetchGame();
  }, [lessonId]);

  const fetchGame = async () => {
    try {
      const res = await fetch(`${API_URL}/games/vocabulary/${lessonId}`);
      const data = await res.json();

      if (data.error) {
        alert(data.error);
        return;
      }

      setGameData(data.questions);
      setCurrentQuestion(0);
      setScore(0);
      setIsFinished(false);
    } catch (error) {
      console.error("Hiba a játék betöltésekor:", error);
    }
  };

  const handleAnswer = (answer) => {
    setSelectedAnswer(answer);
    setShowResult(true);

    const isCorrect = answer === gameData[currentQuestion].correct_answer;
    if (isCorrect) {
      setScore(score + 1);
    }

    // Következő kérdés 2 másodperc múlva
    setTimeout(() => {
      setShowResult(false);
      setSelectedAnswer(null);

      if (currentQuestion < gameData.length - 1) {
        setCurrentQuestion(currentQuestion + 1);
      } else {
        setIsFinished(true);
      }
    }, 2000);
  };

  if (!gameData) {
    return <div>Betöltés...</div>;
  }

  if (isFinished) {
    return (
      <div style={{ textAlign: "center", padding: "2rem" }}>
        <h2>🎉 Játék vége!</h2>
        <p style={{ fontSize: "2rem" }}>
          Eredmény: {score} / {gameData.length}
        </p>
        <button onClick={fetchGame} style={{ marginTop: "1rem" }}>
          Újra játszom
        </button>
      </div>
    );
  }

  const question = gameData[currentQuestion];

  return (
    <div style={{ maxWidth: "600px", margin: "0 auto", padding: "2rem" }}>
      <div style={{ marginBottom: "2rem" }}>
        <p style={{ fontSize: "0.9rem", color: "#666" }}>
          Kérdés {currentQuestion + 1} / {gameData.length}
        </p>
        <p style={{ fontSize: "0.9rem", color: "#666" }}>
          Pontszám: {score}
        </p>
      </div>

      <div style={{ marginBottom: "2rem" }}>
        <h2 style={{ fontSize: "2rem", marginBottom: "1rem" }}>
          {question.question}
        </h2>
        {question.example && (
          <p style={{ fontStyle: "italic", color: "#555", fontSize: "0.9rem" }}>
            {question.example}
          </p>
        )}
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
        {question.options.map((option, index) => {
          let buttonStyle = {
            padding: "1rem",
            fontSize: "1.1rem",
            cursor: showResult ? "default" : "pointer",
            border: "2px solid #ddd",
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

      {showResult && (
        <div
          style={{
            marginTop: "2rem",
            padding: "1rem",
            borderRadius: "8px",
            backgroundColor:
              selectedAnswer === question.correct_answer ? "#dcfce7" : "#fee2e2",
            textAlign: "center",
          }}
        >
          {selectedAnswer === question.correct_answer ? (
            <p style={{ color: "#16a34a", fontWeight: "bold" }}>✓ Helyes!</p>
          ) : (
            <p style={{ color: "#dc2626", fontWeight: "bold" }}>
              ✗ Helyes válasz: {question.correct_answer}
            </p>
          )}
        </div>
      )}
    </div>
  );
}