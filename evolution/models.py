from __future__ import annotations
from typing import List

class ObjectModel():
    def __init__(self, id:int, name:str, weight:int, value:int) -> None:
        self.id:int = id
        self.name:str = name
        self.weight:int = weight
        self.value:int = value

class ChromosomeModel():
    def __init__(self, gene:List[bool]) -> None:
        self.gene:List[bool] = gene
        self.fitness:int = 0
        self.probability:float = 0
        
    def __lt__(self, other: ChromosomeModel):
         return self.fitness['f'] < other.fitness['f']
    
    def __repr__(self) -> str:
        return ' '.join([str(int(c)) for c in self.gene])