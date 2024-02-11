import sys
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
    def min_distance(self, dist, spt_set):
        min_dist = sys.maxsize
        min_index = 0
        for v in range(self.V):
            if dist[v] < min_dist and spt_set[v] == False:
                min_dist = dist[v]
                min_index = v
        return min_index
    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        spt_set = [False] * self.V
        for cout in range(self.V):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and spt_set[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.print_solution(dist)
    def print_solution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])
V = int(input("Enter the number of vertices: "))
g = Graph(V)
print("Enter the adjacency matrix (space-separated entries, use 0 for no edge):")
for i in range(V):
    row = list(map(int, input().split()))
    g.graph[i] = row
src = int(input("Enter the source vertex: "))
g.dijkstra(src)