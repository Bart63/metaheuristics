from typing import List
from helpers import SingletonMeta


class StateMatrix(metaclass=SingletonMeta):
    def __init__(self, roads:List[List[int]]):
        self.places = [r[0] for r in roads]
        self.matrix = [[1] * len(roads) for _ in roads]
        self.set_matrix(roads)
        
    def set_matrix(self, roads:List[List[int]]):
        for r1 in roads:
            for i2, r2 in enumerate(roads[r1[0]:]):
                r = r1[0] - 1
                c = i2 + r1[0]
                self.matrix[r][c] = (
                    (r1[1] - r2[1]) ** 2 + (r1[2] - r2[2]) ** 2
                ) ** 0.5
    
    def copy(self):
        sm_copy = StateMatrix([])
        sm_copy.places = self.places
        sm_copy.matrix = self.matrix
        return sm_copy
