from collections import defaultdict
# only for connected graphs
class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        visited = [False] * len(self.graph)

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end="")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        print('\r')

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end="")

        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_util(i, visited)

    def dfs(self):
        visited = [False] * len(self.graph)
        for i in range(len(self.graph) - 1):
            if visited[i] == False:
                self.dfs_util(i, visited)

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 4)

#g.bfs(2)
g.dfs()