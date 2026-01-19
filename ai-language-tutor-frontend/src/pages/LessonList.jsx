import { useEffect, useState } from "react";
import { getLessons } from "../api/lessonApi";

export default function LessonList() {
  const [lessons, setLessons] = useState([]);

  useEffect(() => {
    getLessons().then(data => {
      console.log("API válasz:", data);
      setLessons(data);
    });
  }, []);

  return (
    <div>
      <h1>Témakörök</h1>
      <ul>
        {lessons.map(lesson => (
          <li key={lesson.id}>{lesson.title}</li>
        ))}
      </ul>
    </div>
  );
}
