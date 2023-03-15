from graph import Graph, graph_from_file
import sys 
sys.setrecursionlimit(5000000)

data_path = "input/"
file_name = "network.1.in"

g = graph_from_file(data_path + file_name)
#print(g)

#print(Graph.connected_components_set(g))
print(Graph.get_path_with_power(g, 3, 4, 20000000))
print(Graph.min_distance(g, 3, 4, 2000000))
#print([0]*5)