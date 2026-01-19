import { useState } from "react";
import LessonList from "./pages/LessonListUpdated";
import VocabularyGame from "./components/VocabularyGame";

function App() {
  const [selectedLesson, setSelectedLesson] = useState(null);

  if (selectedLesson) {
    return (
      <div>
        <button
          onClick={() => setSelectedLesson(null)}
          style={{
            margin: "1rem",
            padding: "0.5rem 1rem",
            cursor: "pointer"
          }}
        >
          ← Vissza a leckékhez
        </button>
        <VocabularyGame lessonId={selectedLesson} />
      </div>
    );
  }

  return <LessonList onSelectLesson={setSelectedLesson} />;
}

export default App;