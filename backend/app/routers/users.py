from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])


class UserLogin(BaseModel):
    name: str


@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    """Bejelentkezés/regisztráció név alapján"""
    user = crud.get_user_by_name(db, user_data.name)

    if not user:
        # Ha nincs ilyen user, létrehozzuk
        user = crud.create_user(db, name=user_data.name)

    return {
        "id": str(user.id),
        "name": user.name,
        "is_premium": user.is_premium,
        "level": user.level
    }


@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@router.post("/")
def create_user(name: str, age: int = None, level: str = "beginner", db: Session = Depends(get_db)):
    return crud.create_user(db, name, age, level)


@router.post("/{user_id}/upgrade-premium")
def upgrade_to_premium(user_id: str, db: Session = Depends(get_db)):
    """Prémium státusz aktiválása"""
    user = crud.update_user_premium(db, user_id, True)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": str(user.id),
        "name": user.name,
        "is_premium": user.is_premium,
        "level": user.level
    }