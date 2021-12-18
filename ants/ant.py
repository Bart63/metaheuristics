from random import choice
from statematrix import StateMatrix
from random import random

class Ant:
    def __init__(self, places_count:int):
        self.left = list(range(places_count))
        self.visited = []
        self.choose_random_place()
        
    def choose_random_place(self):
        chosen = choice(self.left)
        self.visited.append(chosen)
        self.left.remove(chosen)

    def get_traveled_distance(self, sm:StateMatrix):
        pairs = [sorted([v1, v2]) for v1, v2 in zip(self.visited[:-1], self.visited[1:])]
        distance = sum([sm.matrix[p[0]][p[1]] for p in pairs])
        return distance
    
    def roulette_selection(self, probabilities):
        value_sum = 0
        lottery = random()
        for idx, place in enumerate(self.left):
            value_sum += probabilities[idx]
            if lottery < value_sum:
                return place
        return self.left[-1]
    
    def visit_place_prob(self, sm:StateMatrix, alfa, beta):
        cur_place = self.visited[-1]

        probabilities = []
        for place in self.left:
            idxs = sorted([cur_place, place])
            road_pher = sm.matrix[idxs[1]][idxs[0]] ** alfa
            road_heur = (1 / sm.matrix[idxs[0]][idxs[1]]) ** beta
            prob = road_pher * road_heur
            probabilities.append(prob)

        prob_sum = sum(probabilities)
        if prob_sum == 0:
            prob_sum = float("1e-100")
        probabilities = [p/prob_sum for p in probabilities]

        chosen = self.roulette_selection(probabilities)
        self.visited.append(chosen)
        self.left.remove(chosen)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Ant):
            return False
        o: Ant = o
        return self.visited == o.visited
