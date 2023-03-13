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
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
#Il faut dans un premier temps verifier que les noeuds sont dans le graph sinon on les ajoutes 
        
        if node1 not in self.graph.keys() :
            self.graph[node1]=[]
            self.nodes.append(node1)
            self.nb_nodes +=1
        if node2 not in self.graph.keys() :
            self.graph[node2]=[]
            self.nodes.append(node2)
            self.nb_nodes +=1

        self.graph[node1].append((node2, power_min, dist)) #On ajoute la relation a partir de la 1ere extremité de l'arrete 
        self.graph[node2].append((node1, power_min, dist)) # On ajoute également de l'autre coté ( vice versa)
        self.nb_edges +=1
    
    
    def connected_components(self):
        """
        return a list of all the conected components of a graph
        """
        #création d'un dictionnaire permettant de voir si un noeud est visité
        visited={i:False for i in self.nodes} 

        def exploration(s):
            #this function return all the nodes of a graph explorated from an initial one
                L=[s] # list of the connected nodes
                s_neigh = [self.graph[s][j][0] for j in range(0,len(self.graph[s]))] #list of the node's neighbours
                for neigh in s_neigh: 
                    if not visited[neigh] : #for each neighbor not visited
                        visited[neigh]=True 
                        L=L+ exploration(neigh) 
                return L

        Components = []
        N= self.nodes
        for node in N :
            if visited[node]==False : 
                Components.append(exploration(node))
        return Components

    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component),
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))  




    def path_power(self, src, dest, power):
        precedent= {i:None for i in self.nodes}
        traiter= {j:False for j in self.nodes}
        distance= {k:float('inf') for k in self.nodes}  
        distance[src] = 0
        a_traiter = [(0, src)]
        while a_traiter: 
            dist_noeud, noeud= a_traiter.pop()
            if not traiter[noeud] :
                traiter[noeud] = True
                neigh = [self.graph[noeud][j] for j in range(0,len(self.graph[noeud]))]
                for voisin in neigh:
                    powermin = voisin[1]
                    if power >= powermin:
                        dist_voisin = dist_noeud + voisin[2]
                        if dist_voisin < distance[voisin[0]]:
                            distance[voisin[0]] = dist_voisin
                            precedent[voisin[0]] = noeud
                            a_traiter.append((dist_voisin, voisin[0]))
            a_traiter.sort(reverse=True) 
        return distance, precedent                    

        
    def get_path_with_power(self, src, dest, power):
        d, p = self.path_power(src, dest, power)
        if p[dest] == None:
           return None
        else:
           T = [dest]
           i= dest 
           while i != src:
            T.append(p[i])
            i= p[i]
        T.reverse()    
        return T




    def min_power(self, src, dest):
        """
        calculates, for a given journey t, the minimum power of a truck that can cover this journey
        Should return path, min_power. 
        
        Args:
            src (int): source, starting node
            dest (int): destinantion
        Output :
        path (list)
        min_power (int)

        """
        explo=[((src,0),[src])] # format : [(node,pw_min),[path]]
        list_paths = [] # list of the paths between the nodes
        while explo : 
            node, path = explo.pop(0) # it allows us to update the paths used
            n_neigh = [self.graph[node[0]][j] for j in range(0,len(self.graph[node[0]]))] #list of (node's neighbours,powermin,dist)
            for neighb in n_neigh : 
                powermin = neighb[1]
                if neighb[0] not in path :  #for each neighbor not yet in the path
                    if neighb[0] == dest:
                        list_paths.append((path + [neighb[0]],max(node[1],powermin)))
                    else:
                        explo.append(((neighb[0],max(node[1],powermin)), path + [neighb[0]]))

        mini= float('inf')
        for chm in list_paths : #loop to recover the minimum power
            if chm[1]<= mini :
                path_result = chm

        return None if path_result ==[] else path_result[0],path_result[1]


def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    g: Graph
        An object of the class Graph with the graph from file_name.
    """
    with open(filename, "r") as file:
        n, m = map(int, file.readline().split())
        g = Graph(range(1, n+1))
        for _ in range(m):
            edge = list(map(int, file.readline().split()))
            if len(edge) == 3:
                node1, node2, power_min = edge
                g.add_edge(node1, node2, power_min,1) # will add dist=1 by default
            elif len(edge) == 4:
                node1, node2, power_min, dist = edge
                g.add_edge(node1, node2, power_min, dist)
            else:
                raise Exception("Format incorrect")
    return g



    