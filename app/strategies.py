from typing import List
from .models import Film

# base strategy

class SortStrategy:
    def sort(self, films: List[Film]) -> List[Film]:
        raise NotImplementedError("Необходимо реализовать метод sort")
    
class SortStrategyByTitle(SortStrategy):
    def sort(self, films: List[Film]) -> List[Film]:
        return sorted(films, key=lambda film: film.title)

class SortStrategyByYear(SortStrategy):
    def sort(self, films: List[Film]) -> List[Film]:
        return sorted(films, key=lambda film: film.year)
    
class SortStrategyByAuthor(SortStrategy):
    def sort(self, films: List[Film]) -> List[Film]:
        return sorted(films, key=lambda film: film.author)
    
# pick for sort

class FilmSorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy
