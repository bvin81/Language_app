import { useState, useEffect, useRef } from "react";

const API_URL = import.meta.env.VITE_API_URL;

export default function SpeakingGame({ lessonId, user }) {
  const [words, setWords] = useState([]);
  const [lessonLanguage, setLessonLanguage] = useState("romanian");
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isListening, setIsListening] = useState(false);
  const [transcript, setTranscript] = useState("");
  const [score, setScore] = useState(0);
  const [showResult, setShowResult] = useState(false);
  const [resultType, setResultType] = useState(null); // 'correct', 'partial', 'wrong'
  const [isFinished, setIsFinished] = useState(false);
  const [isSupported, setIsSupported] = useState(true);
  const [attempts, setAttempts] = useState(0);
  const [playbackSpeed, setPlaybackSpeed] = useState(0.7);

  const recognitionRef = useRef(null);

  useEffect(() => {
    // Ellenőrizzük a Web Speech API támogatását
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
      setIsSupported(false);
      return;
    }

    // Speech Recognition inicializálása
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognitionRef.current = new SpeechRecognition();
    recognitionRef.current.continuous = false;
    recognitionRef.current.interimResults = false;

    recognitionRef.current.onresult = (event) => {
      const result = event.results[0][0].transcript.toLowerCase().trim();
      setTranscript(result);
      handleResult(result);
    };

    recognitionRef.current.onerror = (event) => {
      console.error("Speech recognition error:", event.error);
      setIsListening(false);
      if (event.error === 'no-speech') {
        setTranscript("Nem hallottam semmit. Próbáld újra!");
      }
    };

    recognitionRef.current.onend = () => {
      setIsListening(false);
    };

    fetchLessonInfo();
    fetchWords();

    return () => {
      if (recognitionRef.current) {
        recognitionRef.current.abort();
      }
    };
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

  const fetchWords = async () => {
    try {
      const res = await fetch(`${API_URL}/lessons/${lessonId}/words`);
      const data = await res.json();

      if (data.length === 0) {
        return;
      }

      // Random 5 szó kiválasztása
      const shuffled = data.sort(() => 0.5 - Math.random());
      setWords(shuffled.slice(0, Math.min(5, shuffled.length)));
      setCurrentIndex(0);
      setScore(0);
      setIsFinished(false);
      setAttempts(0);
    } catch (error) {
      console.error("Hiba a szavak betöltésekor:", error);
    }
  };

  const startListening = () => {
    if (!recognitionRef.current) return;

    setTranscript("");
    setShowResult(false);
    setAttempts(attempts + 1);

    // Nyelv beállítása a lecke alapján
    recognitionRef.current.lang = getLanguageCode();

    setIsListening(true);
    recognitionRef.current.start();
  };

  const stopListening = () => {
    if (recognitionRef.current) {
      recognitionRef.current.stop();
    }
    setIsListening(false);
  };

  const handleResult = (spokenText) => {
    const currentWord = words[currentIndex];
    const targetWord = currentWord.word.toLowerCase().trim();

    // Egyszerű összehasonlítás
    const similarity = calculateSimilarity(spokenText, targetWord);

    setShowResult(true);

    if (similarity >= 0.9) {
      setResultType('correct');
      setScore(score + 1);
    } else if (similarity >= 0.6) {
      setResultType('partial');
      setScore(score + 0.5);
    } else {
      setResultType('wrong');
    }

    setTimeout(() => {
      nextWord();
    }, 2500);
  };

  const calculateSimilarity = (str1, str2) => {
    // Levenshtein távolság alapú hasonlóság
    const longer = str1.length > str2.length ? str1 : str2;
    const shorter = str1.length > str2.length ? str2 : str1;

    if (longer.length === 0) return 1.0;

    const distance = levenshteinDistance(longer, shorter);
    return (longer.length - distance) / longer.length;
  };

  const levenshteinDistance = (str1, str2) => {
    const matrix = [];

    for (let i = 0; i <= str2.length; i++) {
      matrix[i] = [i];
    }
    for (let j = 0; j <= str1.length; j++) {
      matrix[0][j] = j;
    }

    for (let i = 1; i <= str2.length; i++) {
      for (let j = 1; j <= str1.length; j++) {
        if (str2.charAt(i - 1) === str1.charAt(j - 1)) {
          matrix[i][j] = matrix[i - 1][j - 1];
        } else {
          matrix[i][j] = Math.min(
            matrix[i - 1][j - 1] + 1,
            matrix[i][j - 1] + 1,
            matrix[i - 1][j] + 1
          );
        }
      }
    }

    return matrix[str2.length][str1.length];
  };

  const nextWord = () => {
    setShowResult(false);
    setTranscript("");
    setAttempts(0);

    if (currentIndex < words.length - 1) {
      setCurrentIndex(currentIndex + 1);
    } else {
      saveProgress(Math.round(score), words.length);
      setIsFinished(true);
    }
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

  const speakWord = () => {
    if ('speechSynthesis' in window) {
      speechSynthesis.cancel(); // Előző lejátszás leállítása

      const currentWord = words[currentIndex];
      const utterance = new SpeechSynthesisUtterance(currentWord.word);

      // Nyelv beállítása a lecke alapján
      utterance.lang = getLanguageCode();
      utterance.rate = playbackSpeed;
      utterance.pitch = 1;

      speechSynthesis.speak(utterance);
    }
  };

  const getSpeedLabel = () => {
    if (playbackSpeed <= 0.5) return "Nagyon lassú";
    if (playbackSpeed <= 0.7) return "Lassú";
    if (playbackSpeed <= 0.9) return "Normál";
    return "Gyors";
  };

  if (!isSupported) {
    return (
      <div style={{ textAlign: "center", padding: "2rem" }}>
        <h2>Beszéd gyakorlás</h2>
        <p style={{ color: "#dc2626" }}>
          Sajnos a böngésződ nem támogatja a beszédfelismerést.
        </p>
        <p style={{ color: "#666", fontSize: "0.9rem" }}>
          Próbáld meg Chrome vagy Edge böngészőben!
        </p>
      </div>
    );
  }

  if (!words || words.length === 0) {
    return (
      <div style={{ textAlign: "center", padding: "2rem" }}>
        <h2>Beszéd gyakorlás</h2>
        <p>Ehhez a leckéhez még nincsenek szavak.</p>
      </div>
    );
  }

  if (isFinished) {
    const percentage = Math.round((score / words.length) * 100);
    return (
      <div style={{ textAlign: "center", padding: "2rem" }}>
        <h2>🎤 Beszéd gyakorlás vége!</h2>
        <p style={{ fontSize: "2rem" }}>
          Eredmény: {Math.round(score)} / {words.length}
        </p>
        <p style={{
          fontSize: "1.5rem",
          color: percentage >= 80 ? "#16a34a" : percentage >= 50 ? "#ea580c" : "#dc2626"
        }}>
          {percentage}%
        </p>
        <p style={{ marginTop: "1rem", color: "#666" }}>
          {percentage >= 80 ? "Kiváló kiejtés! 🌟" :
           percentage >= 50 ? "Jó munka! Gyakorolj tovább a kiejtésen!" :
           "Ne add fel! Hallgasd meg és ismételd a szavakat!"}
        </p>
        <button
          onClick={fetchWords}
          style={{
            marginTop: "1rem",
            padding: "0.75rem 1.5rem",
            cursor: "pointer",
            backgroundColor: "#ec4899",
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

  const currentWord = words[currentIndex];

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
            Szó {currentIndex + 1} / {words.length}
          </p>
          <p style={{ fontSize: "0.9rem", color: "#666", margin: 0 }}>
            Pontszám: {Math.round(score)}
          </p>
        </div>
        <div style={{
          backgroundColor: "#fce7f3",
          padding: "0.5rem 1rem",
          borderRadius: "20px",
          fontSize: "0.85rem",
          color: "#be185d"
        }}>
          🎤 {lessonLanguage === "romanian" ? "Román" : "Angol"} kiejtés
        </div>
      </div>

      {/* Szó megjelenítése */}
      <div style={{
        marginBottom: "2rem",
        padding: "2rem",
        backgroundColor: "#fdf2f8",
        borderRadius: "20px",
        border: "3px solid #f9a8d4",
        textAlign: "center"
      }}>
        <h2 style={{
          fontSize: "2.5rem",
          color: "#be185d",
          marginBottom: "0.5rem"
        }}>
          {currentWord.word}
        </h2>
        <p style={{
          fontSize: "1.2rem",
          color: "#666",
          marginBottom: "1rem"
        }}>
          ({currentWord.translation})
        </p>

        {/* Kiejtés meghallgatása */}
        <button
          onClick={speakWord}
          style={{
            padding: "0.75rem 1.5rem",
            fontSize: "1rem",
            cursor: "pointer",
            backgroundColor: "#f472b6",
            color: "white",
            border: "none",
            borderRadius: "25px",
            display: "inline-flex",
            alignItems: "center",
            gap: "0.5rem"
          }}
        >
          🔊 Meghallgatom
        </button>

        {/* Sebesség csúszka */}
        <div style={{
          marginTop: "1.5rem",
          padding: "1rem",
          backgroundColor: "#fce7f3",
          borderRadius: "10px"
        }}>
          <label style={{
            display: "block",
            marginBottom: "0.5rem",
            fontSize: "0.9rem",
            color: "#be185d",
            fontWeight: "bold"
          }}>
            🎚️ Kiejtés sebessége: {getSpeedLabel()} ({playbackSpeed.toFixed(1)}x)
          </label>
          <input
            type="range"
            min="0.3"
            max="1.2"
            step="0.1"
            value={playbackSpeed}
            onChange={(e) => setPlaybackSpeed(parseFloat(e.target.value))}
            style={{
              width: "100%",
              height: "8px",
              cursor: "pointer",
              accentColor: "#ec4899"
            }}
          />
          <div style={{
            display: "flex",
            justifyContent: "space-between",
            fontSize: "0.75rem",
            color: "#9f1239",
            marginTop: "0.25rem"
          }}>
            <span>Lassú</span>
            <span>Normál</span>
            <span>Gyors</span>
          </div>
        </div>
      </div>

      {/* Felvétel gomb */}
      <div style={{ textAlign: "center", marginBottom: "2rem" }}>
        {!isListening ? (
          <button
            onClick={startListening}
            disabled={showResult}
            style={{
              padding: "1.5rem 3rem",
              fontSize: "1.3rem",
              cursor: showResult ? "default" : "pointer",
              backgroundColor: showResult ? "#94a3b8" : "#ec4899",
              color: "white",
              border: "none",
              borderRadius: "50px",
              display: "inline-flex",
              alignItems: "center",
              gap: "0.75rem",
              boxShadow: "0 6px 20px rgba(236, 72, 153, 0.4)"
            }}
          >
            🎤 Mondd ki!
          </button>
        ) : (
          <button
            onClick={stopListening}
            style={{
              padding: "1.5rem 3rem",
              fontSize: "1.3rem",
              cursor: "pointer",
              backgroundColor: "#ef4444",
              color: "white",
              border: "none",
              borderRadius: "50px",
              display: "inline-flex",
              alignItems: "center",
              gap: "0.75rem",
              animation: "pulse 1.5s infinite"
            }}
          >
            ⏹️ Befejezem
          </button>
        )}

        {isListening && (
          <p style={{
            marginTop: "1rem",
            color: "#ec4899",
            fontSize: "1.1rem",
            animation: "pulse 1.5s infinite"
          }}>
            🎧 Figyelek... Mondd ki a szót!
          </p>
        )}
      </div>

      {/* Eredmény */}
      {showResult && (
        <div style={{ marginTop: "1rem" }}>
          {/* Amit mondtál */}
          <div style={{
            padding: "1rem",
            backgroundColor: "#f1f5f9",
            borderRadius: "12px",
            marginBottom: "1rem",
            textAlign: "center"
          }}>
            <p style={{ margin: 0, color: "#64748b", fontSize: "0.9rem" }}>
              Amit mondtál:
            </p>
            <p style={{ margin: "0.5rem 0 0", fontSize: "1.3rem", fontWeight: "bold" }}>
              "{transcript}"
            </p>
          </div>

          {/* Értékelés */}
          <div style={{
            padding: "1.5rem",
            borderRadius: "15px",
            textAlign: "center",
            backgroundColor: resultType === 'correct' ? "#dcfce7" :
                           resultType === 'partial' ? "#fef3c7" : "#fee2e2",
            border: `3px solid ${
              resultType === 'correct' ? "#4ade80" :
              resultType === 'partial' ? "#fbbf24" : "#f87171"
            }`
          }}>
            {resultType === 'correct' && (
              <>
                <p style={{ fontSize: "2rem", margin: 0 }}>🌟</p>
                <p style={{ color: "#16a34a", fontWeight: "bold", margin: "0.5rem 0 0" }}>
                  Tökéletes kiejtés!
                </p>
              </>
            )}
            {resultType === 'partial' && (
              <>
                <p style={{ fontSize: "2rem", margin: 0 }}>👍</p>
                <p style={{ color: "#d97706", fontWeight: "bold", margin: "0.5rem 0 0" }}>
                  Majdnem! Gyakorolj még!
                </p>
              </>
            )}
            {resultType === 'wrong' && (
              <>
                <p style={{ fontSize: "2rem", margin: 0 }}>💪</p>
                <p style={{ color: "#dc2626", fontWeight: "bold", margin: "0.5rem 0 0" }}>
                  Próbáld újra! A helyes kiejtés: "{currentWord.word}"
                </p>
              </>
            )}
          </div>
        </div>
      )}

      {/* Tippek */}
      <div style={{
        marginTop: "2rem",
        padding: "1rem",
        backgroundColor: "#fef3c7",
        borderRadius: "12px",
        fontSize: "0.9rem",
        color: "#92400e"
      }}>
        <p style={{ margin: 0 }}>
          💡 <strong>Tipp:</strong> Először hallgasd meg a szót, majd próbáld utánozni!
          Beszélj tisztán és lassan.
        </p>
      </div>
    </div>
  );
}
