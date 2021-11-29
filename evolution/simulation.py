from evolution.models import ChromosomeModel, ObjectModel
from filemanager import FileManager
from typing import List, Dict, Tuple
from itertools import product
from simstat import SimStat
from time import time_ns
import evolution as ev
import helpers as hlp

ms_to_ns = 1000000

selection_methods:List[Dict] = [
    {'roulette': lambda *args: ev.roulette_selection(*args)},
    {'ranking': lambda *args: ev.ranking_selection(*args)},
    {'tournament': lambda *args: ev.tournament_selection(*args)},
    {'elite': lambda *args: ev.elite_selection(*args)}
]

crossover_methods:List[Dict] = [
    {'singlepoint': lambda *args: ev.single_point_crossover(*args)},
    {'twopoint': lambda *args: ev.two_point_crossover(*args)},
    {'uniform': lambda *args: ev.uniform_crossover(*args)}
]

unieque_methods:List[Tuple[Dict, Dict]] = list(product(selection_methods, crossover_methods))


def add_stat(stat:SimStat, population:List[ChromosomeModel], stagnation_lvl:int):
    fitnesses = [p.fitness for p in population]
    stat.add_values(fitnesses)
    stat.add_stagnation_lvl(stagnation_lvl)


def simulate_configuration(objects:List[ObjectModel], param:Dict, methods:Tuple, 
max_gen:int, repeats:int, tournament_size:int, max_stagn:int, params_idx:int, knapsack_capacity:int):
    population_size = param['population_size']
    mutation_prob = param['mutation_probability']
    crossover_prob = param['crossover_probability']
    selection_size = hlp.calc_selection_size(crossover_prob, population_size)
    sm, cm = methods
    select_name = hlp.get_name(sm)
    crossover_name = hlp.get_name(cm)
    
    print(f"Simulate configuration with operations: {select_name}, {crossover_name}")
    print(f"Population size: {population_size}")
    print()
    for repetition in range(repeats):
        print(f"Simulation repetition: {repetition}/{repeats-1}")
        start_time = time_ns()
        stagnometer:int = 0
        simstat = SimStat(crossover_prob, mutation_prob, population_size, max_gen, select_name, crossover_name, params_idx, repetition)
        # Generate first population
        population:List[ChromosomeModel] = ev.generate_population(population_size, objects, knapsack_capacity)
        # Calculate fitness
        ev.calculate_fitness(population, objects, knapsack_capacity)
        population.sort(reverse=True)
        best_chromosom:ChromosomeModel = population[0].copy()
        add_stat(simstat, population, stagnometer)
        for __ in range(max_gen):
            # Choose parents
            choosen_parents:List[ChromosomeModel] = hlp.get_fun(sm)(population, selection_size, tournament_size)
            # Create children
            children:List[ChromosomeModel] = []
            for chrom1, chrom2 in hlp.pairwise(choosen_parents):
                res:Tuple[ChromosomeModel, ChromosomeModel] = hlp.get_fun(cm)(chrom1, chrom2)
                children.extend(list(res))
            # Mutate children
            for child in children:
                ev.mutate(child, mutation_prob)
            # Fill up next generation
            missing_chromosomes:int = population_size - len(children)
            next_generation:List[ChromosomeModel] = children
            for _ in range(missing_chromosomes-1):
                next_chromosome:ChromosomeModel = ev.ranking_selection(population, 1)[0]
                population.remove(next_chromosome)
                next_generation.append(next_chromosome)
            population = next_generation
            # Calculate fitness
            ev.calculate_fitness(population, objects, knapsack_capacity)
            # Get best chromosome
            population.sort(reverse=True)
            if population[0] > best_chromosom:
                best_chromosom = population[0].copy()
                stagnometer = 0
            else:
                stagnometer += 1
            add_stat(simstat, population, stagnometer)
            if stagnometer >= max_stagn:
                break
        duration_ms = round((time_ns() - start_time) / ms_to_ns, 3)
        simstat.add_time_stat_ms(duration_ms)
        FileManager().save_stats(simstat)
    print()


def main():
    txt_manager = FileManager()
    objects:List[ObjectModel] = txt_manager.get_input()

    conf:Dict = txt_manager.get_conf()
    repeat_sim:int = conf['repeat_simulation']
    tournament_size:int = conf['tournament_size']
    max_stagnation:int = conf['max_stagnation']
    knapsack_capacity:int = conf['knapsack_capacity']
    params:List[Dict] = conf['parameters']
    max_gens:int = conf['max_generations']

    # Run simulations with all genetic operators and written parameters
    for um in unieque_methods:
        for idx, param in enumerate(params):
            simulate_configuration(objects, param, um, max_gens, repeat_sim, tournament_size, max_stagnation, idx, knapsack_capacity)


if __name__ == '__main__':
    main()
