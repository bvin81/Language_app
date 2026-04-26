# AI Language Tutor

A full-stack web application for interactive language learning. Features five game-based exercise types, speech synthesis and recognition, progress tracking, and an admin content management panel.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python + FastAPI |
| Database | SQLite + SQLAlchemy |
| Frontend | React 19 + Vite |
| Speech | Web Speech API (synthesis + recognition) |
| Packaging | PyInstaller (desktop build) |

---

## Key Features

- **5 exercise types** — Vocabulary flashcards, Grammar fill-in, Reading comprehension, Listening (TTS audio), Speaking (speech-to-text grading)
- **Levenshtein-based pronunciation scoring** — speaking answers graded by edit distance, three-tier feedback
- **Progress tracking** — per-user statistics, completion rates, lesson history
- **Admin panel** — CRUD for lessons, words, grammar and listening exercises
- **Freemium model** — first 3 lessons free, premium unlock via user flag
- **Desktop packaging** — distributable `.exe` via PyInstaller (`.spec` included)

---

## Architecture

```
├── backend/
│   └── app/
│       ├── main.py           # FastAPI entry point, CORS, router registration
│       ├── database.py       # SQLAlchemy engine + session
│       ├── crud.py           # Reusable DB operations
│       ├── models/           # ORM: User, Lesson, Word, Grammar, Listening, Reading, Progress
│       └── routers/          # users, lessons, words, games, progress, admin
│
└── ai-language-tutor-frontend/
    └── src/
        ├── App.jsx           # Routing, auth wrapper
        ├── api/lessonApi.js  # Axios API calls
        ├── components/       # VocabularyGame, GrammarGame, SpeakingGame, ListeningGame, ReadingGame
        └── pages/            # LessonList, Statistics, AdminPanel
```

---

## API Overview

```
POST /users/login                          # Register or login by name
GET  /lessons/                             # All lessons with metadata
GET  /games/vocabulary/{lesson_id}         # Vocabulary exercise set
GET  /games/grammar/{lesson_id}            # Grammar exercise set
GET  /games/listening/{lesson_id}          # Listening exercise set
GET  /games/reading/{lesson_id}            # Reading exercise set
POST /games/check-answer                   # Validate answer
POST /progress/                            # Save result
GET  /progress/{user_id}                   # User statistics
POST /admin/lessons                        # Admin: create lesson
```

---

## Local Setup

```bash
# Backend
cd backend
pip install -r requirements.txt
python init.py                             # seed database
uvicorn app.main:app --reload              # http://localhost:8000

# Frontend
cd ai-language-tutor-frontend
npm install
npm run dev                                # http://localhost:5173
```

---

## License

[CC BY-NC 4.0](LICENSE) — free to use for learning and non-commercial purposes.
Portfolio project by [bvin81](https://github.com/bvin81).
