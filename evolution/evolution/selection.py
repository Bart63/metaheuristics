from typing import List, Tuple
from evolution.models import ChromosomeModel
from random import random, shuffle


def calculate_probability_roulette(chromosomes:List[ChromosomeModel]):
    fitness_sum = sum(chromosome.fitness
        for chromosome in chromosomes
    )
    if fitness_sum > 0:
        for chromosom in chromosomes:
            chromosom.probability = chromosom.fitness/fitness_sum
        return
    common_prob = 1/len(chromosomes)
    for chromosom in chromosomes:
        chromosom.probability = common_prob


def calculate_probability_ranking(chromosomes:List[ChromosomeModel]):
    fitness_position_list = list(set(c.fitness for c in chromosomes))
    fitness_position_list.sort()
    
    fitness_list_sum = sum([
        idx * len([c for c in chromosomes if c.fitness==fl]) 
        for idx, fl in enumerate(fitness_position_list)
    ])
    if fitness_list_sum == 0:
        fitness_list_sum = len(chromosomes)
        fitness_position_list = [1] + fitness_position_list 
    
    for chromosom in chromosomes:
        chromosom.probability = fitness_position_list.index(chromosom.fitness) / fitness_list_sum


def roulette_prep(chromosomes:List[ChromosomeModel]) -> List[Tuple[ChromosomeModel, float, float]]:
    ranges = []
    value_sum = 0
    for c in chromosomes:
        ranges.append((c, value_sum, value_sum+c.probability))
        value_sum += c.probability
    return ranges


def roulette_select(ranges:List[Tuple[ChromosomeModel, float, float]]) -> ChromosomeModel:
    lottery = random()
    for r in ranges:
        if r[1] <= lottery < r[2]:
            return r[0]
    return ranges[-1][0]


def roulette_generator(chromosomes:List[ChromosomeModel], roulette_size:int) -> List[ChromosomeModel]:
    ranges = roulette_prep(chromosomes)
    return [
        roulette_select(ranges)
        for _ in range(roulette_size)
    ]

def validate_size(chromosomes:List[ChromosomeModel], generation_size:int) -> int:
    if 1 <= generation_size <= len(chromosomes):
        return generation_size
    if generation_size < 1:
        return 1
    return len(chromosomes)

def roulette_selection(chromosomes:List[ChromosomeModel], generation_size:int, *args) -> List[ChromosomeModel]:
    generation_size = validate_size(chromosomes, generation_size)
    calculate_probability_roulette(chromosomes)
    return roulette_generator(chromosomes, generation_size)


def ranking_selection(chromosomes:List[ChromosomeModel], generation_size:int, *args) -> List[ChromosomeModel]:
    generation_size = validate_size(chromosomes, generation_size)
    calculate_probability_ranking(chromosomes)
    return roulette_generator(chromosomes, generation_size)
    

def tournament_select(chromosomes:List[ChromosomeModel], tournament_size:int) -> ChromosomeModel:
    chromosomes_copy = chromosomes.copy()
    shuffle(chromosomes_copy)
    tournament_group = chromosomes_copy[:tournament_size]
    tournament_group.sort(reverse=True)
    return tournament_group[0]


def tournament_selection(chromosomes:List[ChromosomeModel], generation_size:int, tournament_size:int) -> ChromosomeModel:
    generation_size = validate_size(chromosomes, generation_size)
    tournament_size = validate_size(chromosomes, tournament_size)
    return [
        tournament_select(chromosomes, tournament_size)
        for _ in range(generation_size)
    ]


def elite_selection(chromosomes: List[ChromosomeModel], generation_size:int, *args) -> List[ChromosomeModel]:
    generation_size = validate_size(chromosomes, generation_size)
    chromosomes_copy = chromosomes.copy()
    chromosomes_copy.sort(reverse=True)
    return chromosomes_copy[:generation_size]
