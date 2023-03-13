class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.parent = nodes
        self.rang = [0] * nodes

        
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i: int, j: int):
        parent_i = self.find(i)
        parent_j = self.find(j)
        if parent_i == parent_j:
            return
        if self.rang[parent_i] < self.rang[parent_j]:
            self.parent[parent_i] = parent_j
        elif self.rang[parent_i] > self.rang[parent_j]:
            self.parent[parent_j] = parent_i
        else:
            self.parent[parent_j] = parent_i
            self.rang[parent_i] += 1

    def kruskal(self):
        g_mst = {i:i for i in self.nodes}
        
        for u in range(self.nodes):
            for v, weight in graph.adj_list[u]:
                edges.put((weight, u, v))
        uf = UnionFind(graph.num_vertices)
        while not edges.empty():
            weight, u, v = edges.get()
            if uf.find(u) != uf.find(v):
                mst.add_edge(u, v, weight)
                uf.union(u, v)
        return mst