
from evolution.models import ChromosomeModel, ObjectModel
from random import shuffle
from typing import List, Dict

chromosomes_counter:Dict[ChromosomeModel,int] = {}
chromosome_instances_limit = 3

def generate_chromosom(objects:List[ObjectModel], knapsack_capacity:int) -> ChromosomeModel:
    chromosome_length = len(objects)
    prospective_genes = [False] * chromosome_length

    idxs = list(range(0, chromosome_length))
    shuffle(idxs)
    idx = idxs.pop()
    weight = objects[idx].weight
    while weight <= knapsack_capacity:
        prospective_genes[idx] = True
        idx = idxs.pop()
        weight += objects[idx].weight

        if not idxs:
            break
        if weight > knapsack_capacity and not sum(prospective_genes):
            weight = 0
    
    prospective_chromosome = ChromosomeModel(prospective_genes)

    if prospective_chromosome not in chromosomes_counter:
        chromosomes_counter[prospective_chromosome] = 1
        return prospective_chromosome
        
    if chromosomes_counter[prospective_chromosome] > chromosome_instances_limit:
        return generate_chromosom(objects, knapsack_capacity)

    chromosomes_counter[prospective_chromosome] += 1
    return prospective_chromosome


def generate_population(population_size:int, objects:List[ObjectModel], knapsack_capacity:int) -> List[ChromosomeModel]:
    return [
        generate_chromosom(objects, knapsack_capacity)
        for _ in range(population_size)
    ]
