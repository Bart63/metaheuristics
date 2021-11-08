import graphrep as gr
from os.path import join, dirname, realpath
from input_manager import TXTManager
    
outputfolder = join(dirname(realpath(__file__)), 'output')

def save_adjacency_matrix(param_dict, GraphRepr: gr.GraphRepr):
    number_of_vertices = param_dict['vertices']
    edges = param_dict['edges']
    graph = GraphRepr
    
    for _ in range(number_of_vertices):
        graph.add_vertex()
   
    for v1, v2 in edges:
        graph.add_edge(v1, v2)
    
    adj_mat_file = open(join(outputfolder, 'adjacencymatrix.txt'), 'w')
    for line in graph.graph:
        adj_mat_file.write(', '.join(map(str, line)))

def main():
    save_adjacency_matrix(TXTManager().get_input(), gr.DirAdjacencyMatrix())

if __name__ == '__main__':
    main()
    