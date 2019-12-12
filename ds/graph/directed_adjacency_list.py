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

    def dfs(self, N):
        visited = [False] * N
        for i in range(N):
            if visited[i] == False:
                self.dfs_util(i, visited)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")
        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_util(i, visited)

    def bfs_disc(self, N):
        visited = [False] * N
        for i in range(N):
            if visited[i] == False:
                self.bfs_util_disc(i, visited)

    def bfs_util_disc(self, v, visited):
        queue = []
        queue.append(v)
        visited[v] = True

        while queue:
            v = queue.pop(0)
            print(v, end=' ')

            for i in self.graph[v]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def topological_sort(self, N):
        visited = [False] * N
        stack = []
        for i in range(N):
            if visited[i] == False:
                self.top_util(i, visited, stack)
        print(stack)

    def top_util(self, v, visited, stack):
        visited[v] =  True

        for i in self.graph[v]:
            if visited[i] == False:
                self.top_util(i, visited, stack)
        stack.insert(0, v)

g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.topological_sort(6)