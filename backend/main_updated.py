from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import users, lessons, words, games

app = FastAPI(title="AI Language Tutor API")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
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

@app.get("/")
def root():
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