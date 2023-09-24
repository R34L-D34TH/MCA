from collections import deque

# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Function for Breadth-First Search
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    if start == goal:
        return "Start and goal are the same."

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    return new_path

            visited.add(node)

    return "No path found."

start_node = 'A'
goal_node = 'F'
result = bfs(graph, start_node, goal_node)
print("BFS Path:", result)
