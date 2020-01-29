class State():

    UNSEEN = 0
    LOOKING_AT = 1
    SEEN = 2

class Vertex():

    def __init__(self, key, state = State.UNSEEN):
        self.key = key
        self.adj = dict()
        self.state = state

    def add_edge(self, v, weight = 0):
        self.adj[v] = weight

class Graph():

    def __init__(self, directed = True):
        self.vertices = dict()
        self.v_count = 0
        self.directed = directed

    def add_vertex(self, key):
        self.v_count += 1
        self.vertices[key] = Vertex(key)

    def get_vertex(self, v):
        if v in self.vertices:
            return self.vertices[v]
        else:
            return None

    def add_edge(self, u, v, weight = 0):
        if u not in self.vertices:
            self.add_vertex(u)
        if v not in self.vertices:
            self.add_vertex(v)
        self.vertices[u].add_edge(self.vertices[v])
        if not self.directed:
            self.vertices[v].add_edge(self.vertices[u])

    def reset_states(self):
        for v in iter(self):
            v.state = State.UNSEEN

def build_graph(projects, dependencies):
    g = Graph(True)
    for project in projects:
        g.add_vertex(project)
    for before, after in dependencies:
        g.add_edge(before, after)
    return g