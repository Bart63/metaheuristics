from typing import List

class SimStat():
    def __init__(self, cross_prob:float, mutat_prob:float, pop_size:int, max_gen:int, 
    sel_met:str, cross_met:str, params_idx:int, repetition:int) -> None:
        self.crossover_probability:float = cross_prob
        self.mutation_probability:float = mutat_prob
        self.population_size:int = pop_size
        self.max_generations:int = max_gen
        self.selection_method:str = sel_met
        self.crossover_method:str = cross_met
        self.parameters_index:int = params_idx
        self.repetition:int = repetition+1
        self.duration_time_ms:float = 0
        self.max_value_per_iteration:List[int] = []
        self.zero_fitness_per_iteration:List[int] = []
        self.stagnatnation_level:List[int] = []
    
    def add_values(self, fitnesses:List[int]):
        self.max_value_per_iteration.append(max(fitnesses))
        self.zero_fitness_per_iteration.append(sum([f==0 for f in fitnesses]))
    
    def add_stagnation_lvl(self, stagnation_lvl:int):
        self.stagnatnation_level.append(stagnation_lvl)
    
    def add_time_stat_ms(self, duration_time:float):
        self.duration_time_ms = duration_time
