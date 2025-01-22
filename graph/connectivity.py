from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    #add edge
    def add_edge(self, u, v):
        self.graph[u].append(v)

    #check connectivity
    def is_reachable(self, s, d):
        visited = [False] * (self.V)

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            n = queue.pop(0)

            if n == d:
                return True

            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        return False


# Create a graph given in the above diagram
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

u = 1
v = 3
if g.is_reachable(u, v):
    print("There is a path from %d to %d" % (u,v))
else :
    print("There is no path from %d to %d" % (u,v))