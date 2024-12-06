from fastapi import FastAPI
from .films import router as films_router
from .database import Base, engine

# Инициализация базы данных
Base.metadata.create_all(bind=engine)

# Создание приложения
app = FastAPI()

# Подключение маршрутов
app.include_router(films_router, prefix="/films", tags=["films"])