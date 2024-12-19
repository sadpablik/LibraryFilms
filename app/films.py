from typing import Optional, List
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
@router.post("/", response_model=Films)
def create_film(film: FilmsCreate, db: Session = Depends(get_db)):
    db_film = FilmFactory.create(title=film.title, author=film.author, year=film.year, genre=film.genre)
    db.add(db_film)
    db.commit()
    db.refresh(db_film)
    return db_film


@router.get("/", response_model=List[Films])
def get_films(db: Session = Depends(get_db)):
    films = db.query(Film).all() 
    return films

@router.get("/{film_id}", response_model=Films)
def get_film(film_id: int, db: Session = Depends(get_db)):
    db_film = db.query(Film).filter(Film.id == film_id).first()  
    if db_film is None:
        raise HTTPException(status_code=404, detail="Film not found")
    return db_film

@router.get("/author/{author_name}", response_model=List[Films])
def get_films_by_author(author_name: str, db: Session = Depends(get_db)):
    db_films = db.query(Film).filter(Film.author == author_name).all()
    if not db_films:
        raise HTTPException(status_code=404, detail="Films by this author not found")
    return db_films

@router.get("/title/{film_title}", response_model=List[Films])
def get_films_by_title(film_title: str, db: Session = Depends(get_db)):
    db_films = db.query(Film).filter(Film.title.ilike(f"%{film_title}%")).all()  # Case-insensitive search
    if not db_films:
        raise HTTPException(status_code=404, detail="Films with this title not found")
    return db_films

@router.get("/year/{year}", response_model=List[Films])
def get_films_by_year(year: int, db: Session = Depends(get_db)):
    db_films = db.query(Film).filter(Film.year == year).all()
    if not db_films:
        raise HTTPException(status_code=404, detail="Films from this year not found")
    return db_films