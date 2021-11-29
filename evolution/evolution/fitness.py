from typing import List
from evolution.models import ObjectModel, ChromosomeModel


def calculate_fitness(chromosomes:List[ChromosomeModel], objects:List[ObjectModel], knapsack_capacity:int):
    for chromosome in chromosomes:
        weight_sum, value_sum = 0, 0
        for idx, gene in enumerate(chromosome.genes):
            if gene:
                weight_sum += objects[idx].weight
                value_sum += objects[idx].value
            if weight_sum > knapsack_capacity:
                chromosome.fitness = 0
                break
        else:
            chromosome.fitness = value_sum
