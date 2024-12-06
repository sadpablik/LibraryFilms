from .database import SessionLocal
from .models import Film

def populate_db():
    db = SessionLocal()

    films = [
        Film(title="Inception", author="Christopher Nolan", year=2010, genre="Sci-Fi"),
        Film(title="The Matrix", author="Lana Wachowski, Lilly Wachowski", year=1999, genre="Sci-Fi"),
        Film(title="Interstellar", author="Christopher Nolan", year=2014, genre="Sci-Fi"),
        Film(title="The Godfather", author="Francis Ford Coppola", year=1972, genre="Crime"),
        Film(title="Pulp Fiction", author="Quentin Tarantino", year=1994, genre="Crime")
    ]

    db.add_all(films)
    db.commit()
    db.close()

if __name__ == "__main__":
    populate_db()