from os.path import join
from helpers import SingletonMeta
from os import listdir, remove, getcwd
from json import dump
from simstat import SimStat

OUTPUT_FOLDER = 'output'
get_path = lambda name: join(getcwd(), name)


class FileManager(metaclass=SingletonMeta):
    def __init__(self):
        super(FileManager, self).__init__()
        self.output_path:str = get_path(OUTPUT_FOLDER)
        self.clear_stats()

    def clear_stats(self):
        filelist = [f for f in listdir(self.output_path) if f.endswith(".json") ]
        for f in filelist:
            remove(join(self.output_path, f))

    def save_stats(self, obj:SimStat):
        filename = f"{obj.equation_name}_{obj.particles_count}_{int(obj.inertia_weight*10)}_{int(obj.cognitive_coef*10)}_{int(obj.social_coef*10)}.json"
        print(f'Saving file {filename}')
        path = join(self.output_path, filename)
        with open(path, 'w') as f:
            dump(vars(obj), f)
