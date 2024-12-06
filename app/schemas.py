from pydantic import BaseModel

class FilmsBase(BaseModel):
    title: str
    author: str
    year: int
    genre: str

class FilmsCreate(FilmsBase):
    pass

class Films(FilmsBase):
    id: int

    class Config:
        from_attributes = True