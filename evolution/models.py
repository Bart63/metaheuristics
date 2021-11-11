from typing import List

class ObjectModel():
    def __init__(self, id:int, name:str, weight:int, value:int) -> None:
        self.id:int = id
        self.name:str = name
        self.weight:int = weight
        self.value:int = value

class ChromosomeModel():
    def __init__(self, genes:List[bool]) -> None:
        self.genes:List[bool] = genes
        self.fitness:int = 0
        self.probability:float = 0