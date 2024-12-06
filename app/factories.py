from .models import Film
from .database import SessionLocal

# паттерн factory
class FilmFactory:
    @staticmethod
    def create(title: str, author: str, year: int, genre: str) -> Film:
        """Создание объекта фильма с заданными параметрами."""
        return Film(title=title, author=author, year=year, genre=genre)

# паттерн singleton
class DatabaseSessionSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseSessionSingleton, cls).__new__(cls)
            cls._instance.session = SessionLocal()
        return cls._instance