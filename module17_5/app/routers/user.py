from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.user import User
from models.task import Task
from db import get_db

router = APIRouter()

@router.get("/{user_id}/tasks")
async def tasks_by_user_id(user_id: int, db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.user_id == user_id).all()
    return tasks

@router.delete("/delete/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Удаляем все задачи, связанные с пользователем
    db.query(Task).filter(Task.user_id == user_id).delete()
    db.delete(db_user)
    db.commit()
    return {"detail": "User and all associated tasks deleted"}