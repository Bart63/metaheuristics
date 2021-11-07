import unittest
import graphrep as gr
from graphsolver import GraphSolver

class Test(unittest.TestCase):
    def setUp(self):
        dlist = gr.DirList()
        ulist = gr.UndList()
        damatrix = gr.DirAdjacencyMatrix()
        uamatrix = gr.UndAdjacencyMatrix()
        dimatrix = gr.DirIncidenceMatrix()
        uimatrix = gr.UndIncidenceMatrix()
        dalist = gr.DirAdjacencyList()
        ualist = gr.UndAdjacencyList()

        gs1 = GraphSolver(dlist)
        gs2 = GraphSolver(ulist)
        gs3 = GraphSolver(damatrix)
        gs4 = GraphSolver(uamatrix)
        gs5 = GraphSolver(dimatrix)
        gs6 = GraphSolver(uimatrix)
        gs7 = GraphSolver(dalist)
        gs8 = GraphSolver(ualist)

        self.directed = [gs1, gs3, gs5, gs7]
        self.undirected = [gs2, gs4, gs6, gs8]

        self.all = [gs1, gs3, gs5, gs7, gs2, gs4, gs6, gs8]

        for gs in self.all:
            gs.graph.add_vertex()
            gs.graph.add_vertex()
            gs.graph.add_vertex()
            gs.graph.add_vertex()
            gs.graph.add_vertex()
            gs.graph.add_vertex()
            gs.graph.add_vertex()
            
            gs.graph.add_edge(4, 2)
            gs.graph.add_edge(5, 2)
            gs.graph.add_edge(6, 0)
            gs.graph.add_edge(3, 6)
            gs.graph.add_edge(0, 1)
            gs.graph.add_edge(6, 5)
            gs.graph.add_edge(1, 3)
            gs.graph.add_edge(2, 4)
            gs.graph.add_edge(1, 2)
            gs.graph.add_edge(3, 5)

    def test_bfs_dir(self):
        print()
        print("bfs_directed", end='\n\n')
        bfs = [0, 1, 3, 5]
        res1, res2 = [], []
        for gs in self.directed:
            print("Graph repr: ", gs.graph)
            res = gs.bfs(0, 5)
            res1.append(1 if res == bfs else 0)
            res2.append(1)
            print("Solved with da way: ", res)
            print()
        self.assertListEqual(res1, res2)

    def test_bfs_und(self):
        print()
        print("bfs_undirected", end='\n\n')
        bfs = [0, 6, 5]
        res1, res2 = [], []
        for gs in self.undirected:
            print("Graph repr: ", gs.graph)
            res = gs.bfs(0, 5)
            print("Solved with da way: ", res)
            res1.append(1 if res == bfs else 0)
            res2.append(1)
            print()
        self.assertListEqual(res1, res2)

    def test_dfs_dir(self):
        print()
        print("dfs_directed", end='\n\n')
        dfs = [
            [0, 1, 3, 5],
            [0, 1, 3, 6, 5]
        ]
        res1, res2, res3 = [], [], []
        for gs in self.directed:
            print("Graph repr: ", gs.graph)
            res1 = gs.dfs(0, 5)
            print("Solved with da way: ", res1)
            res2.append(1 if res1 in dfs else 0)
            res3.append(1)
            res1.clear()
            print()
        self.assertListEqual(res3, res2)

    def test_dfs_und(self):
        print()
        print("bfs_undirected", end='\n\n')
        dfs = [
            [0, 1, 2, 5],
            [0, 1, 3, 5],
            [0, 1, 3, 6, 5],
            [0, 6, 3, 5],
            [0, 6, 3, 1, 2, 5],
            [0, 6, 5]
        ]
        res1, res2, res3 = [], [], []
        for gs in self.undirected:
            print("Graph repr: ", gs.graph)
            res1 = gs.dfs(0, 5)
            print("Solved with da way: ", res1)
            res2.append(1 if res1 in dfs else 0)
            res3.append(1)
            res1.clear()
            print()
        self.assertListEqual(res3, res2)


if __name__ == '__main__':
    unittest.main()