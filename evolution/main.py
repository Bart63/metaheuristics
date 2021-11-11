from txt_manager import TXTManager
from typing import List, Tuple
from models import ObjectModel, ChromosomeModel
import globals as glob
from random import randint, seed, random

def generate_population(chromosome_length) -> List[ChromosomeModel]:
    return [ChromosomeModel([
            bool(randint(0, 1)) 
            for __ in range(chromosome_length)
        ]) for _ in range(glob.POPULATION_SIZE)
    ]

def calculate_fitness(chromosomes:List[ChromosomeModel], objects:List[ObjectModel]):
    for chromosome in chromosomes:
        weight_sum, value_sum = 0, 0
        for idx, gene in enumerate(chromosome.genes):
            if gene:
                weight_sum += objects[idx].weight
                value_sum += objects[idx].value
            if weight_sum > glob.KNAPSACK_CAPACITY:
                chromosome.fitness = 0
                break
        else:
            chromosome.fitness = value_sum

def calculate_probability_roulette(chromosomes:List[ChromosomeModel]):
    fitness_sum = sum(chromosome.fitness
        for chromosome in chromosomes
    )
    for chromosom in chromosomes:
        chromosom.probability = chromosom.fitness/fitness_sum

def roulette_prep(chromosomes:List[ChromosomeModel]) -> List[Tuple[ChromosomeModel, float, float]]:
    ranges = []
    value_sum = 0
    for c in chromosomes:
        ranges.append((c, value_sum, value_sum+c.probability))
        value_sum += c.probability
    return ranges

def roulette_selection(chromosomes:List[ChromosomeModel]) -> ChromosomeModel:
    ranges = roulette_prep(chromosomes)
    lottery = random()
    for r in ranges:
        if r[1] <= lottery < r[2]:
            return r[0]

def point_crossover(parent1: ChromosomeModel, parent2: ChromosomeModel) -> List[ChromosomeModel]:
    choose_point = lambda: randint(1, len(parent1.genes)-1)
    point = choose_point()
    children = [
        ChromosomeModel(parent1.genes[:point] + parent2.genes[point:]),
        ChromosomeModel(parent2.genes[:point] + parent1.genes[point:])
    ] 
    return children


def main():
    seed(1)
    txt_manager = TXTManager()
    headers, objects = txt_manager.get_input()

    for i, h in enumerate(headers):
        print(h)
        for obj in objects:
            print(
                obj.id if i==0 else obj.name if i==1
                else obj.weight if i==2 else obj.value
            )
        print('\n')

    chromosome_length = len(objects)
    start_population = generate_population(chromosome_length)
    calculate_fitness(start_population, objects)
    calculate_probability_roulette(start_population)
    selected = [
        roulette_selection(start_population),
        roulette_selection(start_population)
    ]
    print(selected[0].genes)
    print(selected[1].genes)
    children = point_crossover(*selected)
    print(children[0].genes)
    print(children[1].genes)

if __name__=='__main__':
    main()