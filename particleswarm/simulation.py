from particle import Particle
from swarm import Swarm
import params as parameters
from filemanager import FileManager
from typing import List, Dict, Tuple
from itertools import product
from simstat import SimStat


def simulate(params):
    best_positions:List[Tuple[float, float]] = []
    best_adaptations:List[float] = []
    all_positions:List[List[Tuple[float, float]]] = []

    swarm = Swarm(params)
    swarm.update_best_particle()
    
    stagnations = 0
    best_particle = swarm.best_particle

    all_positions.append(swarm.get_positions())
    best_positions.append(best_particle.best_pos)
    best_adaptations.append(best_particle.best_adaptation)

    for _ in range(params['max_iterations']):
        swarm.update_swarm_pos()
        swarm.update_best_particle()
        
        if best_particle.best_adaptation == swarm.best_particle.best_adaptation:
            stagnations += 1
            if stagnations == params['max_stagnations']:
                break
        else:
            stagnations = 0
            best_particle = swarm.best_particle

        all_positions.append(swarm.get_positions())
        best_positions.append(best_particle.best_pos)
        best_adaptations.append(best_particle.best_adaptation)
        
    FileManager().save_stats(
        SimStat(params, best_positions, best_adaptations, all_positions)
    )


def main():
    params_dict:Dict[str, List] = parameters.params
    key_names:List[str] = list(params_dict.keys())
    all_combinations_params:List = list(product(*list(params_dict.values())))
    combinations_param_list:Dict = [
        {k:v for k, v in zip(key_names, param)}
        for param in all_combinations_params
    ]

    for params in combinations_param_list:
        simulate(params)


if __name__ == '__main__':
    main()
