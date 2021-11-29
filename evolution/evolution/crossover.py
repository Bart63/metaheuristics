from evolution.models import ChromosomeModel
from random import randint
from typing import Tuple


def single_point_crossover(parent1: ChromosomeModel, parent2: ChromosomeModel) -> Tuple[ChromosomeModel, ChromosomeModel]:
    choose_point = lambda: randint(1, len(parent1.genes)-1)
    point = choose_point()
    children = (
        ChromosomeModel(parent1.genes[:point] + parent2.genes[point:]),
        ChromosomeModel(parent2.genes[:point] + parent1.genes[point:])
    )
    return children


def two_point_crossover(parent1: ChromosomeModel, parent2: ChromosomeModel) -> Tuple[ChromosomeModel, ChromosomeModel]:
    choose_point = lambda: randint(1, len(parent1.genes)-1)
    points = [choose_point(), choose_point()]
    while points[0] == points[1]:
        points[0] = choose_point()
    points.sort()
    children = (
        ChromosomeModel(parent1.genes[:points[0]] + parent2.genes[points[0]:points[1]] + parent1.genes[points[1]:]),
        ChromosomeModel(parent2.genes[:points[0]] + parent1.genes[points[0]:points[1]] + parent2.genes[points[1]:])
    )
    return children


def uniform_crossover(parent1: ChromosomeModel, parent2: ChromosomeModel) -> Tuple[ChromosomeModel, ChromosomeModel]:
    uniform_crossover = [randint(0, 1) for uc in range(len(parent1.genes))]
    genes = [parent1.genes, parent2.genes]
    child1 = ChromosomeModel([
        genes[uc][idx]
        for idx, uc in enumerate(uniform_crossover)
    ])
    child2 = ChromosomeModel([
        genes[not uc][idx]
        for idx, uc in enumerate(uniform_crossover)
    ])
    return child1, child2
