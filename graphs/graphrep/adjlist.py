from graphrep.graphrep import GraphRepr

class DirAdjacencyList(GraphRepr):
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self):
        self.graph[len(self.graph)] = set()

    def add_edge(self, idx1, idx2):
        self.graph[idx1].add(idx2)

    def get_neighbors(self, idx):
        return self.graph[idx]

class UndAdjacencyList(DirAdjacencyList):
    def __init__(self):
        super(UndAdjacencyList, self).__init__()

    def add_edge(self, idx1, idx2):
        super().add_edge(idx1, idx2)
        self.graph[idx2].add(idx1)