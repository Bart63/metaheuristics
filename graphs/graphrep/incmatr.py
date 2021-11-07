from graphrep.graphrep import GraphRepr

class DirIncidenceMatrix(GraphRepr):
    def __init__(self):
        super(DirIncidenceMatrix, self).__init__()
        self.graph = [[]]
        self.edge_start = 1
        self.edge_end = -1
        
    def add_vertex(self):
        if not self.graph[0]:
            self.graph.append([])
            return
            
        self.graph.append(
            [0] * len(self.graph[0])
        )

    def add_edge(self, idx1, idx2):
        for i, v in enumerate(self.graph):
            v.append(self.edge_start if i==idx1 else self.edge_end if i==idx2 else 0)

    def get_neighbors(self, idx):
        neighbors = set()
        for j, e in enumerate(self.graph[idx]):
            if e == self.edge_start:
                for i, v in enumerate(self.graph):
                    if i == idx:
                        continue
                    if v[j] == self.edge_end:
                        neighbors.add(i)
                        break
        return neighbors

class UndIncidenceMatrix(DirIncidenceMatrix):
    def __init__(self):
        super(UndIncidenceMatrix, self).__init__()
        self.edge_end = self.edge_start