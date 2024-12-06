from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import Films, FilmsCreate
from .models import Film
from .database import SessionLocal
from .factories import FilmFactory
from .decorators import log_action
from .strategies import FilmSorter, SortStrategyByTitle, SortStrategyByYear, SortStrategyByAuthor

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@log_action
@router.get("/", response_model=list[Films])
def get_films(sort_by: str = "title", db: Session = Depends(get_db)):
    films = db.query(Film).all()

    # pick sort strategy
    sorter = FilmSorter(SortStrategyByTitle() if sort_by == "title" else SortStrategyByYear() 
                        if sort_by == "year" else SortStrategyByAuthor())
    sorted_films = sorter.strategy.sort(films)
    return sorted_films

@log_action
@router.post("/", response_model=Films)
def create_film(film: FilmsCreate, db: Session = Depends(get_db)):
    db_film = FilmFactory.create(title=film.title, author=film.author, year=film.year, genre=film.genre)
    db.add(db_film)
    db.commit()
    db.refresh(db_film)
    return db_film
