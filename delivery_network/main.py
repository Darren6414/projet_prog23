from graph import Graph, graph_from_file


data_path = "input/"
file_name = "network.03.in"

g = graph_from_file(data_path + file_name)
print(g)

print(Graph.connected_components_set(g))
print(Graph.path_power(g, 1, 4, 20))
print(Graph.get_path_with_power(g, 1, 4, 20))