from os.path import join
from helpers import SingletonMeta
from os import listdir, remove, getcwd
from typing import Dict, List
from json import load, dump
from simstat import SimStat
from os.path import join

INPUT_FOLDER = 'input'
OUTPUT_FOLDER = 'output'
PARAMS_FNAME = 'params.json'
get_path = lambda name: join(getcwd(), name)


class FileManager(metaclass=SingletonMeta):

    def __init__(self):
        super(FileManager, self).__init__()
        self.inputs_rel:List[str] = listdir(get_path(INPUT_FOLDER))
        self.output_path:str = get_path(OUTPUT_FOLDER)
        #self.clear_stats()
        
    def get_inputs(self) -> Dict[str, List[List[int]]]:
        inputs = {}
        for in_rel in self.inputs_rel:
            temp_input = open(join(INPUT_FOLDER, in_rel)).readlines()
            temp_input = [list(map(int, ti.split())) for ti in temp_input]
            for row in temp_input:
                if len(row) != 3:
                    raise Exception(f'Bad number of input elements. Expected 3. Got {len(row)}')
            inputs[in_rel] = temp_input
        return inputs

    def get_params(self) -> Dict[str, List]:
        return load(open(get_path(PARAMS_FNAME)))

    def clear_stats(self):
        filelist = [f for f in listdir(self.output_path) if f.endswith(".json") ]
        for f in filelist:
            remove(join(self.output_path, f))

    def save_stats(self, obj:SimStat):
        filename = f"{obj.input_name}_{obj.ants_count}_{obj.pheromone_weight}_{obj.heuristic_weight}_{str(obj.evaporation_coef).split('.')[1]}.json"
        print(f'Saving file {filename}')
        path = join(self.output_path, filename)
        with open(path, 'w') as f:
            dump(vars(obj), f)
