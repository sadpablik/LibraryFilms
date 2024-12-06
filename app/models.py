from sqlalchemy import Column, Integer, String
from .database import Base

class Film(Base):
    __tablename__ = "films"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer)
    genre = Column(String)