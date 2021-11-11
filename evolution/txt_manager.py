from ntpath import realpath
from os.path import join, realpath, dirname
import globals as glob
from models import ObjectModel
from typing import List, Tuple
from sys import exit
import io

class TXTManager():
    def __init__(self):
        super(TXTManager, self).__init__()
        self.input_path:str = join(dirname(realpath(__file__)), 'input')
        self.filename:str = glob.INPUT_FILENAME
        
    def get_input(self) -> Tuple[List[str], List[ObjectModel]]:
        path = join(self.input_path, self.filename)
        self.file = io.open(path, encoding='utf8')
        self.headers:List[str] = self.get_headers()
        self.objects:List[ObjectModel] = self.get_objects()
        self.file.close()
        return self.headers, self.objects

    def cast_int_positivie(self, value:str):
        try:
            value = value.replace(' ', '')
            res = int(value)
            if not res > 0:
                raise Exception
        except:
            print('Error while converting to int, try again')
            exit()
        return res

    def remove_newline_char(self, line:str):
        return line[:-1] if line[-1] == '\n' else line

    def readline(self):
        line = self.file.readline()
        return self.remove_newline_char(line)

    def readlines(self):
        return [
            self.split(line2) for line2 in
            [self.remove_newline_char(line) for line in self.file]
        ]

    def split(self, line:str):
        return line.split('\t')

    def get_headers(self):
        line = self.readline()
        return self.split(line)

    def get_objects(self) -> List[ObjectModel]:
        lines = self.readlines()
        objects = []
        for line in lines:
            for idx in glob.INT_CHECK_INDEXES:
                line[idx] = self.cast_int_positivie(line[idx])
            objects.append(ObjectModel(*line))
        return objects