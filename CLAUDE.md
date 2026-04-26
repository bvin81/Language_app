---
project: CLAUDE
status: active
tags: [project]
created: 2026-04-01
---

# AI Language Tutor – CLAUDE.md

## Projekt áttekintés

Gyerekeknek szóló (tanulási nehézségekkel küzdőkre is optimalizált) román és angol nyelvtanuló webalkalmazás. Interaktív játékokkal és adaptív módszerekkel segíti a tanulást.

**Célközönség:** 1-4. osztályos gyerekek, köztük tanulási nehézségekkel küzdők
**Támogatott nyelvek:** Román, Angol
**Üzleti modell:** Freemium (első 3 lecke ingyenes, többi prémium)
**Verzió:** 0.2.0 (MVP fázis)

---

## Tech stack

### Backend
- **Python + FastAPI** – REST API
- **SQLAlchemy ORM** – adatbázis kezelés
- **SQLite** (fejlesztés) / **PostgreSQL** (produkció)
- **Uvicorn** – ASGI szerver
- Gyökér: `backend/`
- Belépési pont: `backend/app/main.py`
- Adatbázis init: `backend/init.py`
- Tartalom bővítés: `backend/add_grade3_4.py`

### Frontend
- **React 19 + Vite 7**
- Vanilla CSS (gyerekbarát design, Nunito betűtípus)
- Gyökér: `ai-language-tutor-frontend/`
- Belépési pont: `ai-language-tutor-frontend/src/main.jsx`

---

## Projekt struktúra

```
AI_language_tutor/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app, CORS, static
│   │   ├── database.py          # SQLAlchemy konfig
│   │   ├── crud.py              # CRUD műveletek
│   │   ├── models/              # SQLAlchemy modellek
│   │   │   ├── user.py
│   │   │   ├── lesson.py
│   │   │   ├── word.py
│   │   │   ├── progress.py
│   │   │   ├── grammar.py
│   │   │   ├── listening.py
│   │   │   └── reading.py
│   │   ├── routers/             # API végpontok
│   │   │   ├── users.py         # /users
│   │   │   ├── lessons.py       # /lessons
│   │   │   ├── words.py         # /lessons/{id}/words
│   │   │   ├── games.py         # /games (5 játéktípus)
│   │   │   ├── progress.py      # /progress
│   │   │   └── admin.py         # /admin
│   │   └── schemas/             # Pydantic sémák
│   ├── init.py                  # DB seed (1-2. osztály, 12 lecke)
│   ├── add_grade3_4.py          # DB seed (3-4. osztály, 10 lecke)
│   ├── requirements.txt
│   ├── test.db                  # SQLite adatbázis (fejlesztés)
│   └── .env
│
├── ai-language-tutor-frontend/
│   ├── src/
│   │   ├── App.jsx              # Fő komponens, routing
│   │   ├── main.jsx             # Entry point
│   │   ├── api/lessonApi.js     # API kliens
│   │   ├── components/
│   │   │   ├── Login.jsx
│   │   │   ├── VocabularyGame.jsx
│   │   │   ├── GrammarGame.jsx
│   │   │   ├── ListeningGame.jsx
│   │   │   ├── ReadingGame.jsx
│   │   │   └── SpeakingGame.jsx
│   │   ├── pages/
│   │   │   ├── LessonList.jsx
│   │   │   ├── Statistics.jsx
│   │   │   └── AdminPanel.jsx
│   │   └── styles/global.css
│   ├── .env                     # VITE_API_URL=http://127.0.0.1:8000
│   └── vite.config.js
│
├── CLAUDE.md                    # Ez a fájl
├── PROJECT_STATUS.md            # Részletes projekt dokumentáció
└── BUILD.md                     # Build és futtatási útmutató
```

---

## Fejlesztési környezet indítása

### Backend
```bash
cd backend
# Első alkalommal:
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python init.py               # Alap seed (1-2. osztály)
python add_grade3_4.py       # 3-4. osztályos tartalom

# Ezután:
python -m uvicorn app.main:app --reload
# Elérhető: http://127.0.0.1:8000
# API docs: http://127.0.0.1:8000/docs
```

### Frontend
```bash
cd ai-language-tutor-frontend
npm install
npm run dev
# Elérhető: http://localhost:5173
```

### Gyors indítás (ha minden telepítve van)
```bash
start_app.bat
```

---

## Adatbázis tartalom (aktuális)

**1. osztály – Román (beginner):** Familia, Numere, Culori, Casa
**2. osztály – Román (beginner):** Animale, Școala, Mâncarea
**2. osztály – Angol (beginner):** Food, Family, Colors, Animals, School
**3. osztály – Román (intermediate):** Vremea, Corpul uman, Transport
**3. osztály – Angol (intermediate):** Weather, Body Parts, Transport
**4. osztály – Román (advanced):** Natura, Timp liber
**4. osztály – Angol (advanced):** Nature, Hobbies

Összesen: **22 lecke**, ~107 szó, 66 nyelvtani feladat, 44 hallásértés, 22 szöveg (88 kérdés)

---

## API végpontok

| Metódus | Útvonal | Leírás |
|---------|---------|--------|
| POST | `/users/login` | Bejelentkezés/regisztráció név alapján |
| POST | `/users/{id}/upgrade-premium` | Prémium aktiválás |
| GET | `/lessons/` | Összes lecke (language, grade szűrőkkel) |
| GET | `/games/vocabulary/{lesson_id}` | Szókincs játék |
| GET | `/games/grammar/{lesson_id}` | Nyelvtan játék |
| GET | `/games/listening/{lesson_id}` | Hallásértés játék |
| GET | `/games/reading/{lesson_id}` | Szövegértés játék |
| POST | `/games/check-answer` | Válasz ellenőrzés |
| POST | `/progress/` | Eredmény mentése |
| GET | `/progress/{user_id}` | Felhasználó haladása |
| POST | `/admin/lessons` | Lecke létrehozása |
| PUT | `/admin/lessons/{id}` | Lecke módosítása |
| DELETE | `/admin/lessons/{id}` | Lecke törlése |

---

## Adatmodellek

```python
User:    id (UUID), name (unique), age, level, is_premium, is_admin
Lesson:  id, title, description, language, level, grade, order, is_premium
Word:    id, lesson_id, word, translation, example_sentence
GrammarExercise: id, lesson_id, exercise_type, question, correct_answer,
                 wrong_answers (csv), explanation, difficulty (1-3)
ListeningExercise: id, lesson_id, audio_url, transcript, question,
                   correct_answer, wrong_answers, difficulty, duration_seconds
ReadingExercise: id, lesson_id, title, content, difficulty
ReadingQuestion: id, reading_id, question, correct_answer, wrong_answers
Progress: id, user_id, lesson_id, score, total, completed_at
```

---

## Ismert korlátok

- **Nincs jelszó** – bárki beléphet bármilyen névvel
- **TTS minőség** – böngésző beépített TTS, románra gyengébb
- **Speech Recognition** – csak Chrome/Edge-ben működik
- **SQLite** – fejlesztésre ok, produkciónál PostgreSQL kell
- **Audio fájlok** – placeholder URL-ek, valódi mp3-ak nincsenek

---

## Következő prioritások

1. JWT alapú jelszavas autentikáció
2. Valódi audio fájlok (anyanyelvi felvételek)
3. Szülői felügyelet modul
4. Spaced Repetition algoritmus
5. Gamification (jelvények, streak, szintek)
