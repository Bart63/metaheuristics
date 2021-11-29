from os.path import join, realpath, dirname
from evolution import ObjectModel
from helpers import SingletonMeta
from os import listdir, remove
from typing import Dict, List
from json import load, dump
from ntpath import realpath
from simstat import SimStat
from os.path import join
from sys import exit
import io

INPUT_FILENAME = 'objects.txt'
SIMULATION_CONF_FILENAME = 'simulation.json'
INT_CHECK_INDEXES = [0, 2, 3]


class FileManager(metaclass=SingletonMeta):

    def __init__(self):
        super(FileManager, self).__init__()
        self.input_path:str = join(dirname(realpath(__file__)), 'input')
        self.output_path:str = join(dirname(realpath(__file__)), 'output')
        self.filename_input:str = INPUT_FILENAME
        self.filename_conf:str = SIMULATION_CONF_FILENAME
        
    def get_input(self) -> List[ObjectModel]:
        path = join(self.input_path, self.filename_input)
        self.file = io.open(path, encoding='utf8')
        self.headers:List[str] = self.get_headers()
        self.objects:List[ObjectModel] = self.get_objects()
        self.file.close()
        return self.objects

    def get_conf(self) -> Dict:
        self.clear_stats()
        path = join(self.input_path, self.filename_conf)
        conf_json = load(open(path))
        return conf_json

    def clear_stats(self):
        filelist = [f for f in listdir(self.output_path) if f.endswith(".json") ]
        for f in filelist:
            remove(join(self.output_path, f))

    def save_stats(self, obj:SimStat):
        filename = f"{obj.selection_method}_{obj.crossover_method}_{obj.parameters_index}_{obj.max_generations}_{str(obj.repetition).rjust(2, '0')}.json"
        print(filename)
        path = join(self.output_path, filename)
        with open(path, 'w') as f:
            dump(vars(obj), f)
        
    def cast_int_positivie(self, value:str) -> int:
        try:
            value = value.replace(' ', '')
            res = int(value)
            if not res > 0:
                raise Exception
        except:
            print('Error while converting to int, try again')
            exit()
        return res

    def remove_newline_char(self, line:str) -> str:
        return line[:-1] if line[-1] == '\n' else line

    def readline(self) -> str:
        line = self.file.readline()
        return self.remove_newline_char(line)

    def readlines(self) -> List[str]:
        return [
            self.split(line2) for line2 in
            [self.remove_newline_char(line) for line in self.file]
        ]

    def split(self, line:str) -> List[str]:
        return line.split('\t')

    def get_headers(self) -> List[str]:
        line = self.readline()
        return self.split(line)

    def get_objects(self) -> List[ObjectModel]:
        lines = self.readlines()
        objects = []
        for line in lines:
            for idx in INT_CHECK_INDEXES:
                line[idx] = self.cast_int_positivie(line[idx])
            objects.append(ObjectModel(*line))
        return objects
