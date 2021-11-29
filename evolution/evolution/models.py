from __future__ import annotations
from typing import List


class ChromosomeModel:
    def __init__(self, genes:List[bool]) -> None:
        self.genes:List[bool] = genes
        self.fitness:int = 0
        self.probability:float = 0
       
    def __hash__(self) -> int:
        return hash(''.join(list(map(str, map(int, self.genes)))))

    def __lt__(self, other: ChromosomeModel):
         return self.fitness < other.fitness
    
    def __str__(self) -> str:
        return ' '.join([str(int(c)) for c in self.genes])
    
    def __len__(self) -> int:
        return len(self.genes)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, ChromosomeModel):
            return False
        o: ChromosomeModel = o
        return self.genes == o.genes
    
    def copy(self) -> ChromosomeModel:
        copied = ChromosomeModel(self.genes.copy())
        copied.fitness = self.fitness
        self.probability = self.probability
        return copied


class ObjectModel():
    def __init__(self, id:int, name:str, weight:int, value:int) -> None:
        self.id:int = id
        self.name:str = name
        self.weight:int = weight
        self.value:int = value
