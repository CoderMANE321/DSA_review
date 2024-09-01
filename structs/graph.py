class Graph:
    def __init__(self):
        # Initialize an empty graph with an adjacency list
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        # Add a new vertex to the graph
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Add an undirected edge between two vertices
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        # Remove the edge between two vertices
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].remove(vertex2)
            if vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        # Remove a vertex and all associated edges
        if vertex in self.adjacency_list:
            for neighbor in self.adjacency_list[vertex]:
                self.adjacency_list[neighbor].remove(vertex)
            del self.adjacency_list[vertex]

    def dfs(self, start_vertex, visited=None):
        # Depth-First Search (DFS) with backtracking
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex, end=" ")

        for neighbor in self.adjacency_list[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start_vertex):
        # Breadth-First Search (BFS)
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


"""
use

from structs.graph import Graph

graph = Graph()

# Add vertices
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')

# Add edges
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')

# Perform DFS
print("DFS starting from vertex A:")
graph.dfs('A')
print()

# Perform BFS
print("BFS starting from vertex A:")
graph.bfs('A')
print()

# Remove an edge
graph.remove_edge('A', 'B')
print("Graph after removing edge A-B:")
print(graph.adjacency_list)

# Remove a vertex
graph.remove_vertex('D')
print("Graph after removing vertex D:")
print(graph.adjacency_list)
"""