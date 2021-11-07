from graphrep.graphrep import GraphRepr

class DirList(GraphRepr):
    def __init__(self):
        super(DirList, self).__init__()
        
    def add_edge(self, idx1, idx2):
        if [idx1, idx2] not in self.graph:
            self.graph.append([idx1, idx2])

    def get_neighbors(self, idx):
        return set(
            e[1] 
            for e in self.graph
            if e[0] == idx
        )

class UndList(DirList):
    def __init__(self):
        super(UndList, self).__init__()

    def add_edge(self, idx1, idx2):
        order1 = [idx1, idx2] not in self.graph
        order2 = [idx2, idx1] not in self.graph
        if order1 and order2:
            self.graph.append([idx1, idx2])

    def get_neighbors(self, idx):
        neighbors = super().get_neighbors(idx)
        for e in self.graph:
            if e[1] == idx:
                neighbors.add(e[0])
        return neighbors