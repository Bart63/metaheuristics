from util import Stack, Queue
from graphrep import GraphRepr

class GraphSolver:
    def __init__(self, graph: GraphRepr):
        self.graph = graph

    def bfs(self, starting_vertex, destination_vertex):
        visited = set()
        queue = Queue()
        queue.push([starting_vertex])
        while queue.size() > 0:
            curr_path = queue.pop()
            curr_vertex = curr_path[-1]
            if curr_vertex in visited:
                continue
            if curr_vertex == destination_vertex:
                return curr_path
            visited.add(curr_vertex)
            for neighbor in self.graph.get_neighbors(curr_vertex):
                new_path = curr_path.copy()
                new_path.append(neighbor)
                queue.push(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        visited = set()
        stack = Stack()
        stack.push([starting_vertex])
        while stack.size() > 0:
            curr_path = stack.pop()
            curr_vertex = curr_path[-1]
            if curr_vertex in visited:
                continue
            if curr_vertex == destination_vertex: 
                return curr_path
            visited.add(curr_vertex)
            for neighbor in self.graph.get_neighbors(curr_vertex):
                new_path = curr_path.copy()
                new_path.append(neighbor)
                stack.push(new_path)
        return None