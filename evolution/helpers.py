from typing import Dict, Iterable


class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

def calc_selection_size(crossover_prob:float, population_size:int):
    if crossover_prob < 0:
        crossover_prob = 0
    if crossover_prob > 1:
        crossover_prob = 1

    selection_size = round(population_size*crossover_prob)
    if selection_size <= 1:
        selection_size = 2
    elif selection_size%2 == 1:
        selection_size -= 1
    return selection_size


def pairwise(iterable:Iterable):
    a = iter(iterable)
    return zip(a, a)


def get_fun(dict:Dict):
    return list(dict.values())[0]


def get_name(dict:Dict):
    return list(dict.keys())[0]
