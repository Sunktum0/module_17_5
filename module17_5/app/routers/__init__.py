
# ННазаров ПВ
# module_17.py
from .user import User
from .task import Task
from fastapi import APIRouter

# Импортируем роутеры
from .task import router as task_router
from .user import router as user_router

# Создаем главный роутер и объединяем маршруты
router = APIRouter()
router.include_router(task_router)
router.include_router(user_router)