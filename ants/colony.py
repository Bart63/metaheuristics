from typing import List, Dict, Union
from ant import Ant
from statematrix import StateMatrix
from random import random
import sys


class Colony:
    def __init__(self, params:Dict[str, Union[float, int]]):
        self.params = params
        self.best_ant:Ant = None

    def configurate_ants(self, places_count:list):
        ants_count = self.params['ants_count']
        self.colony:List[Ant] = []
        for _ in range(ants_count):
            ant = Ant(places_count)
            ant.choose_random_place()
            self.colony.append(ant)

    def move_ants(self, sm:StateMatrix):
        alfa, beta = self.params['pheromone_weight'], self.params['heuristic_weight']
        for ant in self.colony:
            if random() < self.params['rand_way_prob']:
                ant.choose_random_place()
            else:
                ant.visit_place_prob(sm, alfa, beta)

    def pheromones_update(self, sm:StateMatrix):
        for i1, row in enumerate(sm.matrix[1:]):
            for i2, _ in enumerate(sm.matrix[:i1+1]):
                row[i2] *= (1 - self.params['evaporation_coef'])
                for ant in self.colony:
                    # W prezentacji aktualizuje bez sprawdzenia czy mrówka przeszła daną drogą
                    ri1, ri2 = ant.visited.index(i1), ant.visited.index(i2)
                    if abs(ri1 - ri2) != 1:
                        continue
                    row[i2] += 1/ant.get_traveled_distance(sm)
    
    def save_best_ant(self, sm:StateMatrix):
        best_distance = sys.maxsize if self.best_ant == None else self.best_ant.get_traveled_distance(sm)
        for ant in self.colony:
            distance = ant.get_traveled_distance(sm)
            if distance < best_distance:
                self.best_ant = ant
                best_distance = distance
