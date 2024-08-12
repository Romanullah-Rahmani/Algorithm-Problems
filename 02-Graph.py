def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set on the first call
    
    visited.add(start)  # Mark the start node as visited
    print(start, end=' ')  # Print the current node
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # Recursively visit unvisited neighbors

    return visited  # Return the visited set for potential further use

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS traversal starting from vertex A:")
dfs(graph, 'A')
print()

# =========================================  BFS  ========================================

from collections import deque

def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Initialize a queue with the start node
    visited.add(start)  # Mark the start node as visited
    
    while queue:
        vertex = queue.popleft()  # Dequeue a vertex from the queue
        print(vertex, end=' ')  # Print the current vertex
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark the neighbor as visited
                queue.append(neighbor)  # Enqueue the unvisited neighbor

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS traversal starting from vertex A:")
bfs(graph, 'A')




























# from collections import deque

# class Vertex:
#     def __init__(self, city):
#         # Initialize a vertex with a city name and visited status
#         self.city = city
#         self.was_visited = False
#         self.predecessor = None  # Used to track the shortest path

# class Graph:
#     def __init__(self, max_verts=20):
#         # Initialize the graph with a maximum number of vertices
#         self.max_verts = max_verts
#         self.vertex_list = [None] * self.max_verts  # List to store vertices
#         self.adj_matrix = [[0] * self.max_verts for _ in range(self.max_verts)]  # Adjacency matrix
#         self.n_verts = 0  # Counter for the number of vertices added
#         self.stack = []  # Stack for DFS
#         self.queue = deque()  # Queue for BFS

#     def add_vertex(self, city):
#         # Add a vertex to the graph
#         if self.n_verts < self.max_verts:
#             self.vertex_list[self.n_verts] = Vertex(city)
#             self.n_verts += 1
#         else:
#             raise Exception("Max vertices limit reached")  # Raise an exception if max vertices limit is reached

#     def add_edge(self, start, end):
#         # Add an undirected edge between two vertices
#         if start < self.n_verts and end < self.n_verts:
#             self.adj_matrix[start][end] = 1
#             self.adj_matrix[end][start] = 1
#         else:
#             raise ValueError("Invalid indices for vertices")  # Raise an error if the indices are invalid

#     def display_vertex(self, v):
#         # Display the city name of the vertex
#         print(f"{self.vertex_list[v].city} --> ", end="")

#     def get_adj_unvisited_vertex(self, v):
#         # Get the next unvisited adjacent vertex
#         for j in range(self.n_verts):
#             if self.adj_matrix[v][j] == 1 and not self.vertex_list[j].was_visited:
#                 return j  # Return the index of the adjacent unvisited vertex
#         return -1  # Return -1 if no unvisited adjacent vertex is found

#     def dfs(self):
#         # Depth-First Search (DFS) using an iterative approach
#         self.vertex_list[0].was_visited = True  # Mark the first vertex as visited
#         print(f"From {self.vertex_list[0].city}, you can reach the following cities:")
#         self.stack.append(0)  # Push the first vertex onto the stack

#         while len(self.stack) > 0:
#             v = self.get_adj_unvisited_vertex(self.stack[-1])  # Get the next unvisited adjacent vertex
#             if v == -1:
#                 self.stack.pop()  # Pop the stack if no adjacent unvisited vertex is found
#             else:
#                 self.vertex_list[v].was_visited = True  # Mark the vertex as visited
#                 self.display_vertex(v)  # Display the vertex
#                 self.stack.append(v)  # Push the vertex onto the stack
#         print("End")


#     def recursive_dfs(self, v):
#         # Depth-First Search (DFS) using a recursive approach
#         self.vertex_list[v].was_visited = True  # Mark the vertex as visited
#         self.display_vertex(v)  # Display the vertex

#         for j in range(self.n_verts):
#             if self.adj_matrix[v][j] == 1 and not self.vertex_list[j].was_visited:
#                 self.recursive_dfs(j)  # Recursively visit the adjacent unvisited vertex

#     def bfs(self):
#         self.vertex_list[0].was_visited = True
#         print(f"From {self.vertex_list[0].city}, you can reach the following cities:")
#         queue = deque([0])

#         while queue:
#             current_vertex = queue.popleft()
#             self.display_vertex(current_vertex)

#             while True:
#                 adj_vertex = self.get_adj_unvisited_vertex(current_vertex)
#                 if adj_vertex == -1:
#                     break
#                 self.vertex_list[adj_vertex].was_visited = True
#                 queue.append(adj_vertex)

#         print("End")

#     def find_shortest_path_bfs(self, start, end):
#         # Breadth-First Search (BFS) to find the shortest path between two vertices
#         self.vertex_list[start].was_visited = True  # Mark the starting vertex as visited
#         self.queue.append(start)  # Enqueue the starting vertex

#         while len(self.queue) > 0:
#             v1 = self.queue.popleft()  # Dequeue a vertex

#             for v2 in range(self.n_verts):
#                 if self.adj_matrix[v1][v2] == 1 and not self.vertex_list[v2].was_visited:
#                     self.vertex_list[v2].was_visited = True  # Mark the vertex as visited
#                     self.vertex_list[v2].predecessor = v1  # Set the predecessor to track the path
#                     self.queue.append(v2)  # Enqueue the vertex

#                     if v2 == end:
#                         self.print_shortest_path(start, end)  # Print the shortest path if the end vertex is reached
#                         return

#         print("No path found")  # Print a message if no path is found

#     def print_shortest_path(self, start, end):
#         # Helper method to print the shortest path found by BFS
#         path = []
#         current = end
#         while current is not None:
#             path.append(current)  # Add the current vertex to the path
#             current = self.vertex_list[current].predecessor  # Move to the predecessor
#         path.reverse()  # Reverse the path to get the correct order

#         print("Shortest path from", self.vertex_list[start].city, "to", self.vertex_list[end].city, ":")
#         for v in path:
#             print(self.vertex_list[v].city, end=" --> ")
#         print("End")
    
#     def reset_visited_flags(self):
#         for vertex in self.vertex_list:
#             if vertex is not None:
#                 vertex.was_visited = False
#                 vertex.predecessor = None

# # Example usage:
# if __name__ == "__main__":
#     # Create a graph instance
#     graph = Graph()

#     # Add vertices to the graph
#     graph.add_vertex("Kabul")
#     graph.add_vertex("Ghazni")
#     graph.add_vertex("Jalal Abad")
#     graph.add_vertex("Mazar")
#     graph.add_vertex("Qundoz")

#     # Add edges between vertices
#     graph.add_edge(0, 1)
#     graph.add_edge(1, 2)
#     graph.add_edge(0, 3)
#     graph.add_edge(3, 4)

#     # Perform BFS traversal
#     graph.reset_visited_flags()  # Reset visited flags before
#     print("\nBFS Visits:")
#     graph.bfs()

#     # Perform DFS traversal
#     graph.reset_visited_flags()  # Reset visited flags before
#     print("DFS Visits (Iterative):")
#     graph.dfs()

#     # Find and print the shortest path between two vertices using BFS
#     graph.reset_visited_flags()  # Reset visited flags before
#     graph.find_shortest_path_bfs(0, 4)  # Shortest Path (BFS) from Kabul to Qundoz

#     # Perform recursive DFS traversal
#     graph.reset_visited_flags()  # Reset visited flags before
#     print("\nDFS Visits (Recursive):")
#     graph.recursive_dfs(0)
#     print("End\n")