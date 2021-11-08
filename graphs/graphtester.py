from graphsolver import GraphSolver
import graphrep as gr
from time import  time_ns

nanosec_to_milisec = lambda x: round(x/1000000, 3)

def test_all(param_dict):
    stats = {
        'd_l': test(param_dict, gr.DirList()),
        'u_l': test(param_dict, gr.UndList()),
        'd_a_m': test(param_dict, gr.DirAdjacencyMatrix()),
        'u_a_m': test(param_dict, gr.UndAdjacencyMatrix()),
        'd_i_m': test(param_dict, gr.DirIncidenceMatrix()),
        'u_i_m': test(param_dict, gr.UndIncidenceMatrix()),
        'd_a_l': test(param_dict, gr.DirAdjacencyList()),
        'u_a_l': test(param_dict, gr.UndAdjacencyList())
    }
    return stats

def test(param_dict, GraphRepr: gr.GraphRepr):
    number_of_vertices = param_dict['vertices']
    edges = param_dict['edges']
    start_vertex = param_dict['start']
    end_vertex = param_dict['end']
    graph = GraphRepr
    gs = GraphSolver(graph)

    start = time_ns()
    
    for _ in range(number_of_vertices):
        graph.add_vertex()

    after_add_vertices = time_ns()
   
    for v1, v2 in edges:
        graph.add_edge(v1, v2)

    after_add_edges = time_ns()

    bfs_solution = gs.bfs(start_vertex, end_vertex)

    after_solve_bfs = time_ns()

    dfs_solution = gs.dfs(start_vertex, end_vertex)

    after_solve_dfs = time_ns()

    stats = {
        'time': {
            'add_vertices': nanosec_to_milisec(
                after_add_vertices-start
            ),
            'add_edges': nanosec_to_milisec(
                after_add_edges-after_add_vertices
            ),
            'bfs': nanosec_to_milisec(
                after_solve_bfs-after_add_edges
            ),
            'dfs': nanosec_to_milisec(
                after_solve_dfs-after_solve_bfs
            ),
            'all': nanosec_to_milisec(
                after_solve_dfs-start
            )
        },
        "solution": {
            'bfs': bfs_solution,
            'dfs': dfs_solution
        }
    }
    return stats