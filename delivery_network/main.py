from graph import Graph, graph_from_file
import sys 
sys.setrecursionlimit(5000000)

data_path = "input/"
file_name = "network.3.in"

g = graph_from_file(data_path + file_name)
print(g)

#print(Graph.connected_components_set(g))
#print(Graph.path_power(g, 1, 40, 20000000))
#print(Graph.get_path_with_power(g, 1, 40, 2000000))
print([0]*5)