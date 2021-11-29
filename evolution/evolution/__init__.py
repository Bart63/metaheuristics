"""
Package for implementing evolution algorithm.
"""

__version__ = '1.0'
__author__ = 'Bartosz Durys, Szymon Klewicki'
__description__ = 'Package for implementing evolution algorithm.'

from evolution.crossover import *
from evolution.fitness import *
from evolution.models import ChromosomeModel, ObjectModel
from evolution.mutation import *
from evolution.population import generate_population
from evolution.selection import roulette_selection, ranking_selection, tournament_selection, elite_selection
