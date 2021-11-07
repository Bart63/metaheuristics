from graphrep.graphrep import GraphRepr

class DirAdjacencyMatrix(GraphRepr):
    def __init__(self):
        super(DirAdjacencyMatrix, self).__init__()
        
    def add_vertex(self):
        if not self.graph:
            self.graph.append([0])
            return
        for v in self.graph:
            v.append(0)
        self.graph.append([0] * len(self.graph[0]))

    def add_edge(self, idx1, idx2):
        self.graph[idx1][idx2] = 1

    def get_neighbors(self, idx):
        return set(
            idx2 
            for idx2, v in enumerate(self.graph[idx])
            if v == 1
        )

class UndAdjacencyMatrix(DirAdjacencyMatrix):
    def __init__(self):
        super(UndAdjacencyMatrix, self).__init__()

    def add_edge(self, idx1, idx2):
        super().add_edge(idx1, idx2)
        self.graph[idx2][idx1] = 1