from txt_manager import TXTManager
from typing import List, Tuple
from models import ObjectModel, ChromosomeModel
import globals as glob
import random

def generate_population(chromosome_length) -> List[ChromosomeModel]:
    return [ChromosomeModel([
            bool(random.randint(0, 1)) 
            for __ in range(chromosome_length)
        ]) for _ in range(glob.POPULATION_SIZE)
    ]

def calculate_fitness(chromosomes:List[ChromosomeModel], objects:List[ObjectModel]):
    for chromosome in chromosomes:
        weight_sum, value_sum = 0, 0
        for idx, gene in enumerate(chromosome.gene):
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

def calculate_probability_ranking(chromosomes:List[ChromosomeModel]):
    fitness_position_list = list(set(c.fitness for c in chromosomes))
    fitness_position_list.sort()
    
    fitness_list_sum = sum([
        idx * len([c for c in chromosomes if c.fitness==fl]) 
        for idx, fl in enumerate(fitness_position_list)
    ])
    if fitness_list_sum == 0:
        fitness_list_sum = len(chromosomes)
        fitness_position_list = [0] + fitness_position_list 
    
    for chromosom in chromosomes:
        chromosom.probability = fitness_position_list.index(chromosom.fitness) / fitness_list_sum

def roulette_prep(chromosomes:List[ChromosomeModel]) -> List[Tuple[ChromosomeModel, float, float]]:
    ranges = []
    value_sum = 0
    for c in chromosomes:
        ranges.append((c, value_sum, value_sum+c.probability))
        value_sum += c.probability
    return ranges

def roulette_selection(chromosomes:List[ChromosomeModel]) -> ChromosomeModel:
    ranges = roulette_prep(chromosomes)
    lottery = random.random()
    for r in ranges:
        if r[1] <= lottery < r[2]:
            return r[0]
    else:
        return ranges[-1][0]

def tournament_selection(chromosomes:List[ChromosomeModel]) -> ChromosomeModel:
    chromosomes_copy = chromosomes.copy()
    random.shuffle(chromosomes_copy)
    tournament_group = chromosomes_copy[:glob.TOURNAMENT_SIZE]
    tournament_group.sort()
    return tournament_group[0]

def single_point_crossover(parent1: ChromosomeModel, parent2: ChromosomeModel) -> List[ChromosomeModel]:
    choose_point = lambda: random.randint(1, len(parent1.gene)-1)
    point = choose_point()
    children = [
        ChromosomeModel(parent1.gene[:point] + parent2.gene[point:]),
        ChromosomeModel(parent2.gene[:point] + parent1.gene[point:])
    ] 
    return children

def two_point_crossover(parent1: ChromosomeModel, parent2: ChromosomeModel) -> List[ChromosomeModel]:
    choose_point = lambda: random.randint(1, len(parent1.gene)-1)
    points = [0, 0]
    while points[0] == points[1]:
        points = [choose_point(), choose_point()]
    points.sort()
    children = [
        ChromosomeModel(parent1.gene[:points[0]] + parent2.gene[points[0]:points[1]] + parent1.gene[points[1]:]),
        ChromosomeModel(parent2.gene[:points[0]] + parent1.gene[points[0]:points[1]] + parent2.gene[points[1]:])
    ] 
    return children

def uniform_crossover(parent1: ChromosomeModel, parent2: ChromosomeModel) -> List[ChromosomeModel]:
    uniform_crossover = [random.randint(0, 1) for uc in range(len(parent1.gene))]
    genes = [parent1.gene, parent2.gene]
    child1 = ChromosomeModel([
        genes[uc][idx]
        for idx, uc in enumerate(uniform_crossover)
    ])
    child2 = ChromosomeModel([
        genes[not uc][idx]
        for idx, uc in enumerate(uniform_crossover)
    ])
    return [child1, child2]

def mutate(chromosome: ChromosomeModel):
    gene = chromosome.gene
    for i in range(len(gene)):
        gene[i] = not gene[i] if random.uniform(0, 1) > glob.MUTATION_PROBABILITY else gene[i]

def main():
    random.seed(1)
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
    print([c.probability for c in start_population])
    calculate_probability_ranking(start_population)
    print([c.probability for c in start_population])
    selected = [
        roulette_selection(start_population),
        roulette_selection(start_population)
    ]
    print(selected[0])
    print(selected[1])
    children_spc = single_point_crossover(*selected)
    children_tpc = two_point_crossover(*selected)
    children_uc = uniform_crossover(*selected)
    print("SPC:")
    print(children_spc[0])
    print(children_spc[1])
    print("TPC:")
    print(children_tpc[0])
    print(children_tpc[1])
    print("UC:")
    print(children_uc[0])
    print(children_uc[1])
    copy_gene = str(children_spc[1])
    print('Mutate:')
    mutate(children_spc[1])
    print('Before & after:\n', copy_gene, '\n', children_spc[1])

if __name__=='__main__':
    main()

"""
Jaki model pokoleniowy?
- zastępowanie w każdym pokoleniu części populacji 
czy
- całej

Selekcja rankingowa to selekcja ruletkowa z innym obliczaniem przydziału koła?
Czy eliminujemy z przydziału części koła osobniki, które są na ostatnim miejscu?


"""