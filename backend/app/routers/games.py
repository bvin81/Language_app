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
    Nyelvtani játék placeholder
    TODO: később kifejleszteni nyelvtani szabályokkal
    """
    return {
        "message": "Nyelvtani játék - fejlesztés alatt",
        "lesson_id": lesson_id
    }


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