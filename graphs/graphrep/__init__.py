"""
Package name 'graphrep' stands for graph representation.
Parent class GraphRepr in graphrep.py provides the same functionality among its children
Subclasses follow naming convention:
Dir* - subclass for implementing directed graph representation.
Und* - subclass for implementing undirected graph representation.
idx1 - start node for the edge in a directed graph
idx2 - end node for the edge in a directed graph
"""

__version__ = '1.0'
__author__ = 'Bartosz Durys, Szymon Klewicki'

from graphrep.graphrep import GraphRepr
from graphrep.list import DirList, UndList
from graphrep.adjmatr import DirAdjacencyMatrix, UndAdjacencyMatrix
from graphrep.incmatr import DirIncidenceMatrix, UndIncidenceMatrix
from graphrep.adjlist import DirAdjacencyList, UndAdjacencyList