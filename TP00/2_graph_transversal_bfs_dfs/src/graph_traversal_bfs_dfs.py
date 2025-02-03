from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            queue.extend(graph[node])

    return traversal_order

def dfs_recursive(graph, node, visited=None, traversal_order=None):
    if visited is None:
        visited = set()
        traversal_order = []

    if node not in visited:
        visited.add(node)
        traversal_order.append(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited, traversal_order)

    return traversal_order

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    traversal_order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            stack.extend(reversed(graph[node]))

    return traversal_order

def is_connected(graph, start, end):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == end:
            return True
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])

    return False

def shortest_path(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None

# Example graph with multiple connected components
city_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
    'G': ['H'],
    'H': ['G']
}


# Test BFS and DFS
print("BFS Traversal:", bfs(city_graph, 'A'))
print("DFS Traversal (Recursive):", dfs_recursive(city_graph, 'A'))
print("DFS Traversal (Iterative):", dfs_iterative(city_graph, 'A'))

# Test connectivity and shortest path
print("Is 'A' connected to 'F'?", is_connected(city_graph, 'A', 'F'))
print("Is 'A' connected to 'H'?", is_connected(city_graph, 'A', 'H'))
print("Shortest path from 'A' to 'F':", shortest_path(city_graph, 'A', 'F'))


city_graph = {
          
          0: [1, 2],
          1: [0, 3, 4],
          2: [0, 5],
          3: [1],
          4: [1],
          5: [2]
      
}


# Test BFS and DFS
print("BFS Traversal:", bfs(city_graph, 0))
print("DFS Traversal (Recursive):", dfs_recursive(city_graph, 0))
print("DFS Traversal (Iterative):", dfs_iterative(city_graph, 0))

# Test connectivity and shortest path
print("Is 0 connected to 5?", is_connected(city_graph, 0, 5))
print("Is 1 connected to 5?", is_connected(city_graph, 1, 5))
print("Shortest path from 0 to 5:", shortest_path(city_graph, 0, 5))