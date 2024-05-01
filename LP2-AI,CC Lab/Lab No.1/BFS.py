def bfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    queue = [start]
    visited.add(start)
    print(start)
    while queue:
        current = queue.pop(0)
        for neighbor in graph[current] - visited:
            print(neighbor)
            queue.append(neighbor)
            visited.add(neighbor)
    return visited
def create_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    for node in range(num_nodes):
        graph[str(node)] = set()
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        edge = input("Enter edge (format: node1 node2): ").split()
        node1, node2 = edge
        graph[node1].add(node2)
        graph[node2].add(node1)
    return graph
def main():
    graph = create_graph()
    start_node = input("Enter the start node for BFS: ")
    print("BFS Traversal:")
    bfs(graph, start_node)
if __name__ == "__main__":
    main()