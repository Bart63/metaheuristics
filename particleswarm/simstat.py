from typing import List, Dict, Tuple


class SimStat():
    def __init__(
        self, 
        params:Dict, 
        best_positions:List[Tuple[float, float]],
        best_adaptations:List[float],
        all_positions:List[List[Tuple[float, float]]]
    ):
        self.particles_count:int = params['particles_count']
        
        self.inertia_weight:float = params['inertia_weight']
        self.cognitive_coef:float = params['cognitive_coef']
        self.social_coef:float = params['social_coef']

        self.max_iterations:int = params['max_iterations']
        self.max_stagnations:int = params['max_stagnations']

        self.min_x:float = params['equation_params']['min_x']
        self.max_x:float = params['equation_params']['max_x']
        self.min_y:float = params['equation_params']['min_y']
        self.max_y:float = params['equation_params']['max_y']
        
        self.equation_name:str = list(params['equation_params']['equation'].keys())[0]
        
        self.best_positions = best_positions
        self.best_adaptations = best_adaptations
        self.all_positions = all_positions
