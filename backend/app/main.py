from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pathlib import Path
import os

from app.routers import users, lessons, words, games, progress, admin
from app.database import engine, Base
from app.models.user import User
from app.models.lesson import Lesson
from app.models.word import Word
from app.models.grammar import GrammarExercise
from app.models.listening import ListeningExercise
from app.models.reading import ReadingExercise, ReadingQuestion

# Táblák létrehozása
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Language Tutor API")

# Frontend build útvonal
FRONTEND_BUILD_PATH = Path(__file__).parent.parent.parent / "ai-language-tutor-frontend" / "dist"

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(users.router)
app.include_router(lessons.router)
app.include_router(words.router)
app.include_router(games.router)
app.include_router(progress.router)
app.include_router(admin.router)

# Statikus fájlok (audio, képek stb.)
static_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
if os.path.exists(static_path):
    app.mount("/static", StaticFiles(directory=static_path), name="static")

# Frontend statikus fájlok kiszolgálása (ha létezik a build)
if FRONTEND_BUILD_PATH.exists():
    # Assets mappa (JS, CSS, képek)
    assets_path = FRONTEND_BUILD_PATH / "assets"
    if assets_path.exists():
        app.mount("/assets", StaticFiles(directory=str(assets_path)), name="frontend_assets")


@app.get("/api/info")
def api_info():
    """API információk (fejlesztői célra)."""
    return {
        "message": "AI Language Tutor API",
        "version": "1.0.0",
        "endpoints": {
            "lessons": "/lessons",
            "words": "/lessons/{lesson_id}/words",
            "games": "/games",
            "users": "/users"
        }
    }


@app.get("/{full_path:path}")
async def serve_frontend(request: Request, full_path: str):
    """
    Frontend kiszolgálása - SPA routing támogatás.
    Ha a frontend build létezik, kiszolgálja az index.html-t.
    """
    # API útvonalak kihagyása
    if full_path.startswith(("lessons", "users", "games", "words", "progress", "admin", "docs", "openapi.json", "redoc")):
        return JSONResponse(
            status_code=404,
            content={"detail": "Not found"}
        )

    # Ha nincs frontend build, API info visszaadása
    if not FRONTEND_BUILD_PATH.exists():
        return {
            "message": "AI Language Tutor API",
            "version": "1.0.0",
            "note": "Frontend build not found. Run 'npm run build' in the frontend folder.",
            "docs": "/docs"
        }

    # Konkrét fájl keresése
    file_path = FRONTEND_BUILD_PATH / full_path
    if file_path.is_file():
        return FileResponse(file_path)

    # SPA: minden más útvonalra index.html
    index_path = FRONTEND_BUILD_PATH / "index.html"
    if index_path.exists():
        return FileResponse(index_path)

    return JSONResponse(
        status_code=404,
        content={"detail": "Not found"}
    )