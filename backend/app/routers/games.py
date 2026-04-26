from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Dict
from app.database import get_db
from app import crud
import random

router = APIRouter(prefix="/games", tags=["games"])


@router.get("/vocabulary/{lesson_id}")
def get_vocabulary_game(lesson_id: int, db: Session = Depends(get_db)):
    """
    Szókincs játék: random szavak a leckéből
    Visszaad 5 szót keverten (kérdés + helyes válasz + 3 rossz válasz)
    """
    words = crud.get_words_by_lesson(db, lesson_id)

    if len(words) < 2:
        return {"error": "Nincs elég szó ehhez a leckéhez"}

    game_questions = []
    sample_size = min(5, len(words))
    selected_words = random.sample(words, sample_size)

    for word in selected_words:
        # Helyes válasz
        correct = word.translation

        # 3 rossz válasz más szavakból
        other_words = [w for w in words if w.id != word.id]
        wrong_answers = random.sample([w.translation for w in other_words],
                                      min(3, len(other_words)))

        # Összekeverjük
        options = [correct] + wrong_answers
        random.shuffle(options)

        game_questions.append({
            "question": word.word,
            "example": word.example_sentence,
            "options": options,
            "correct_answer": correct
        })

    return {"questions": game_questions}


@router.get("/grammar/{lesson_id}")
def get_grammar_game(lesson_id: int, db: Session = Depends(get_db)):
    """
    Nyelvtani játék: különböző típusú nyelvtani gyakorlatok
    - fill_blank: Mondatkiegészítés
    - multiple_choice: Helyes forma kiválasztása
    - word_order: Szórend
    """
    exercises = crud.get_grammar_exercises_by_lesson(db, lesson_id)

    if len(exercises) < 1:
        return {"error": "Nincs nyelvtani gyakorlat ehhez a leckéhez", "questions": []}

    game_questions = []
    sample_size = min(5, len(exercises))
    selected_exercises = random.sample(exercises, sample_size)

    for exercise in selected_exercises:
        # Válaszlehetőségek összeállítása
        options = [exercise.correct_answer]

        if exercise.wrong_answers:
            wrong_list = [w.strip() for w in exercise.wrong_answers.split(",")]
            options.extend(wrong_list)

        # Word order típusnál a szavakat keverjük
        if exercise.exercise_type == "word_order":
            # A kérdés tartalmazza a kevert szavakat
            words = [w.strip() for w in exercise.question.split(",")]
            random.shuffle(words)
            question_text = " / ".join(words)
        else:
            question_text = exercise.question

        random.shuffle(options)

        game_questions.append({
            "id": exercise.id,
            "exercise_type": exercise.exercise_type,
            "question": question_text,
            "options": options,
            "correct_answer": exercise.correct_answer,
            "explanation": exercise.explanation,
            "difficulty": exercise.difficulty
        })

    return {"questions": game_questions, "lesson_id": lesson_id}


@router.get("/listening/{lesson_id}")
def get_listening_game(lesson_id: int, db: Session = Depends(get_db)):
    """
    Hallásértés játék: audio fájlok meghallgatása és kérdések megválaszolása
    """
    exercises = crud.get_listening_exercises_by_lesson(db, lesson_id)

    if len(exercises) < 1:
        return {"error": "Nincs hallásértés gyakorlat ehhez a leckéhez", "questions": []}

    game_questions = []
    sample_size = min(5, len(exercises))
    selected_exercises = random.sample(exercises, sample_size)

    for exercise in selected_exercises:
        # Válaszlehetőségek összeállítása
        options = [exercise.correct_answer]
        wrong_list = [w.strip() for w in exercise.wrong_answers.split(",")]
        options.extend(wrong_list)
        random.shuffle(options)

        game_questions.append({
            "id": exercise.id,
            "audio_url": exercise.audio_url,
            "question": exercise.question,
            "options": options,
            "correct_answer": exercise.correct_answer,
            "transcript": exercise.transcript,
            "difficulty": exercise.difficulty,
            "duration_seconds": exercise.duration_seconds
        })

    return {"questions": game_questions, "lesson_id": lesson_id}


@router.get("/reading/{lesson_id}")
def get_reading_game(lesson_id: int, db: Session = Depends(get_db)):
    """
    Szövegértés játék: szöveg olvasása és kérdések megválaszolása
    """
    exercises = crud.get_reading_exercises_by_lesson(db, lesson_id)

    if len(exercises) < 1:
        return {"error": "Nincs szövegértés gyakorlat ehhez a leckéhez", "readings": []}

    readings = []

    for exercise in exercises:
        questions = []
        for q in exercise.questions:
            options = [q.correct_answer]
            wrong_list = [w.strip() for w in q.wrong_answers.split(",")]
            options.extend(wrong_list)
            random.shuffle(options)

            questions.append({
                "id": q.id,
                "question": q.question,
                "options": options,
                "correct_answer": q.correct_answer
            })

        readings.append({
            "reading_id": exercise.id,
            "title": exercise.title,
            "content": exercise.content,
            "difficulty": exercise.difficulty,
            "questions": questions
        })

    return {"readings": readings, "lesson_id": lesson_id}


@router.post("/check-answer")
def check_answer(user_answer: Dict, db: Session = Depends(get_db)):
    """
    Válasz ellenőrzése
    Input: {"question": "...", "user_answer": "...", "correct_answer": "..."}
    """
    is_correct = user_answer.get("user_answer") == user_answer.get("correct_answer")

    return {
        "correct": is_correct,
        "message": "Helyes!" if is_correct else f"Helyes válasz: {user_answer.get('correct_answer')}"
    }