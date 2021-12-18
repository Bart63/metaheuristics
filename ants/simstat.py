from typing import List, Dict, Union


class SimStat():
    def __init__(self, input_name:str, params:Dict[str, Union[float, int]], best_distances:List[int]) -> None:
        self.input_name:str = input_name
        self.ants_count:int = params['ants_count']
        self.pheromone_weight:int = params['pheromone_weight']
        self.heuristic_weight:int = params['heuristic_weight']
        self.evaporation_coef:float = params['evaporation_coef']
        self.best_distances:List[int] = best_distances
