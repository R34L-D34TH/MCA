from queue import PriorityQueue

# Define the graph as an adjacency list with costs
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'D': 2, 'E': 6},
    'C': {'A': 3, 'F': 7},
    'D': {'B': 2},
    'E': {'B': 6, 'F': 4},
    'F': {'C': 7, 'E': 4}
}

# Heuristic function (Euclidean distance to the goal)
def heuristic(node, goal):
    coordinates = {
        'A': (0, 0),
        'B': (2, 2),
        'C': (3, 1),
        'D': (2, 3),
        'E': (4, 3),
        'F': (5, 1)
    }
    x1, y1 = coordinates[node]
    x2, y2 = coordinates[goal]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Function for A* Search
def astar_search(graph, start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    came_from = {}

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                open_set.put((f_score, neighbor))

    return "No path found."

start_node = 'A'
goal_node = 'F'
result = astar_search(graph, start_node, goal_node)
print("A* Search Path:", result)
