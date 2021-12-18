from ant import Ant
from filemanager import FileManager
from typing import List, Dict
from itertools import product
from colony import Colony
from statematrix import StateMatrix
from simstat import SimStat


def simulate(params, sm:StateMatrix, input_file:str):
    stagnations = 0
    best_ant:Ant = None
    best_distances:List[int] = []
    for _ in range(params['max_iterations']):
        colony = Colony(params)
        if best_ant != None:
            colony.best_ant = best_ant

        colony.configurate_ants(len(sm.places))
        for _ in sm.matrix[:-2]:
            colony.move_ants(sm)
        colony.pheromones_update(sm)
        colony.save_best_ant(sm)

        best_distances.append(colony.best_ant.get_traveled_distance(sm))
        if best_ant == colony.best_ant:
            stagnations += 1
            if stagnations == params['max_stagnations']:
                break
        else:
            stagnations = 0
            best_ant = colony.best_ant
    FileManager().save_stats(
        SimStat(input_file.split('.')[0], params, best_distances, best_ant.visited)
    )


def main():
    fm = FileManager()
    input_dict:Dict[str, List[List[int]]] = fm.get_inputs()
    
    params_dict:Dict[str, List] = fm.get_params()
    key_names = list(params_dict.keys())
    all_combinations_params = list(product(*list(params_dict.values())))
    combinations_param_list = [
        {k:v for k, v in zip(key_names, param)}
        for param in all_combinations_params
    ]

    for input_file, start_vals in input_dict.items():
        print()
        print(f"Starting with {input_file} file")
        sm_ = StateMatrix(start_vals)
        for params in combinations_param_list:
            simulate(params, sm_.copy(), input_file)


if __name__ == '__main__':
    main()
