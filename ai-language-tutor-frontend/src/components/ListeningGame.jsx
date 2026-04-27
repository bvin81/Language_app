import { useState, useEffect } from "react";
import { useLanguage } from "../i18n/LanguageContext";

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
  const [playbackSpeed, setPlaybackSpeed] = useState(0.8);
  const { t } = useLanguage();

  useEffect(() => { fetchGame(); fetchLessonInfo(); }, [lessonId]);

  const fetchLessonInfo = async () => {
    try {
      const res = await fetch(`${API_URL}/lessons/`);
      const lessons = await res.json();
      const lesson = lessons.find(l => l.id === lessonId);
      if (lesson) setLessonLanguage(lesson.language);
    } catch (error) {
      console.error("Error loading lesson:", error);
    }
  };

  const fetchGame = async () => {
    try {
      const res = await fetch(`${API_URL}/games/listening/${lessonId}`);
      const data = await res.json();
      if (data.error) return;
      setGameData(data.questions);
      setCurrentQuestion(0);
      setScore(0);
      setIsFinished(false);
      setPlayCount(0);
      setShowTranscript(false);
    } catch (error) {
      console.error("Error loading game:", error);
    }
  };

  const getLanguageCode = () => lessonLanguage === "english" ? "en-US" : "ro-RO";

  const playAudio = () => {
    if (!('speechSynthesis' in window)) { alert(t.noSpeechSupport); return; }
    speechSynthesis.cancel();
    const question = gameData[currentQuestion];
    const utterance = new SpeechSynthesisUtterance(question.transcript);
    utterance.lang = getLanguageCode();
    utterance.rate = playbackSpeed;
    utterance.pitch = 1;
    utterance.onstart = () => setIsPlaying(true);
    utterance.onend = () => setIsPlaying(false);
    utterance.onerror = () => setIsPlaying(false);
    setPlayCount(prev => prev + 1);
    speechSynthesis.speak(utterance);
  };

  const stopAudio = () => { speechSynthesis.cancel(); setIsPlaying(false); };

  const handleAnswer = (answer) => {
    setSelectedAnswer(answer);
    setShowResult(true);
    stopAudio();
    const isCorrect = answer === gameData[currentQuestion].correct_answer;
    if (isCorrect) setScore(score + 1);
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
        body: JSON.stringify({ user_id: user.id, lesson_id: lessonId, score: finalScore, total })
      });
    } catch (error) {
      console.error("Error saving progress:", error);
    }
  };

  const getDifficultyStars = (difficulty) => "⭐".repeat(difficulty);

  const getSpeedLabel = () => {
    if (playbackSpeed <= 0.5) return t.verySlowSpeed;
    if (playbackSpeed <= 0.7) return t.slowSpeed;
    if (playbackSpeed <= 0.9) return t.normalSpeed;
    if (playbackSpeed <= 1.1) return t.fastSpeed;
    return t.veryFastSpeed;
  };

  if (!gameData || gameData.length === 0) {
    return (
      <div style={{ textAlign: "center", padding: "2rem" }}>
        <h2>🎧</h2>
        <p>{t.noListening}</p>
        <p style={{ color: "#666", fontSize: "0.9rem" }}>{t.noListeningSub}</p>
      </div>
    );
  }

  if (isFinished) {
    const percentage = Math.round((score / gameData.length) * 100);
    return (
      <div style={{ textAlign: "center", padding: "2rem" }}>
        <h2>{t.listeningGameOver}</h2>
        <p style={{ fontSize: "2rem" }}>{t.result(score, gameData.length)}</p>
        <p style={{ fontSize: "1.5rem", color: percentage >= 80 ? "#16a34a" : percentage >= 50 ? "#ea580c" : "#dc2626" }}>{percentage}%</p>
        <p style={{ marginTop: "1rem", color: "#666" }}>
          {percentage >= 80 ? t.listeningExcellent : percentage >= 50 ? t.listeningGood : t.listeningKeepGoing}
        </p>
        <button onClick={fetchGame} style={{ marginTop: "1rem", padding: "0.75rem 1.5rem", cursor: "pointer", backgroundColor: "#0891b2", color: "white", border: "none", borderRadius: "8px", fontSize: "1rem" }}>
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
        <div style={{ backgroundColor: "#e0f2fe", padding: "0.5rem 1rem", borderRadius: "20px", fontSize: "0.85rem", color: "#0369a1" }}>
          {getDifficultyStars(question.difficulty)} {lessonLanguage === "romanian" ? t.romanian : t.english}
        </div>
      </div>

      <div style={{ marginBottom: "2rem", padding: "1.5rem", backgroundColor: "#f0f9ff", borderRadius: "12px", border: "2px solid #bae6fd", textAlign: "center" }}>
        <button
          onClick={isPlaying ? stopAudio : playAudio}
          disabled={showResult}
          style={{ padding: "1rem 2rem", fontSize: "1.2rem", cursor: showResult ? "default" : "pointer", backgroundColor: showResult ? "#94a3b8" : isPlaying ? "#ef4444" : "#0891b2", color: "white", border: "none", borderRadius: "50px", display: "flex", alignItems: "center", gap: "0.5rem", margin: "0 auto" }}
        >
          {isPlaying ? t.stopAudio : t.playAudio}
        </button>

        <p style={{ marginTop: "1rem", fontSize: "0.85rem", color: "#64748b" }}>{t.playCount(playCount)}</p>

        <div style={{ marginTop: "1.5rem", padding: "1rem", backgroundColor: "#e0f2fe", borderRadius: "10px" }}>
          <label style={{ display: "block", marginBottom: "0.5rem", fontSize: "0.9rem", color: "#0369a1", fontWeight: "bold" }}>
            {t.playbackSpeed(getSpeedLabel(), playbackSpeed.toFixed(1))}
          </label>
          <input type="range" min="0.3" max="1.5" step="0.1" value={playbackSpeed} onChange={(e) => setPlaybackSpeed(parseFloat(e.target.value))} disabled={isPlaying} style={{ width: "100%", height: "8px", cursor: isPlaying ? "default" : "pointer", accentColor: "#0891b2" }} />
          <div style={{ display: "flex", justifyContent: "space-between", fontSize: "0.75rem", color: "#64748b", marginTop: "0.25rem" }}>
            <span>{t.slowLabel}</span><span>{t.normalLabel}</span><span>{t.fastLabel}</span>
          </div>
        </div>

        {showTranscript && question.transcript && (
          <div style={{ marginTop: "1rem", padding: "1rem", backgroundColor: "#fef3c7", borderRadius: "8px", border: "1px solid #fcd34d" }}>
            <p style={{ margin: 0, fontStyle: "italic", color: "#92400e" }}>📝 "{question.transcript}"</p>
          </div>
        )}
      </div>

      <div style={{ marginBottom: "1.5rem", textAlign: "center" }}>
        <h2 style={{ fontSize: "1.3rem", color: "#0c4a6e" }}>{question.question}</h2>
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
        {question.options.map((option, index) => {
          let buttonStyle = { padding: "1rem", fontSize: "1.1rem", cursor: showResult ? "default" : "pointer", border: "2px solid #bae6fd", borderRadius: "8px", backgroundColor: "#fff", transition: "all 0.2s" };
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
