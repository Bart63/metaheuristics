from evolution.models import ChromosomeModel
from random import sample


def mutate(chromosome: ChromosomeModel, mutation_prob:float):
    if mutation_prob < 0:
        mutation_prob = 0
    elif mutation_prob > 1:
        mutation_prob = 1
    indexes = sample(range(0, len(chromosome)), round(len(chromosome)*mutation_prob))
    gene = chromosome.genes
    for i in indexes:
        gene[i] = not gene[i]
