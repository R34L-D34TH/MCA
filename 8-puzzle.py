from collections import deque

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Define the initial state (example)
initial_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]

# Define possible moves (up, down, left, right)
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Function to find the location of the blank (0) tile
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Function to generate new states by moving the blank
def generate_states(state):
    blank_i, blank_j = find_blank(state)
    new_states = []

    for move in moves:
        new_i, new_j = blank_i + move[0], blank_j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]  # Create a deep copy of the state
            new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
            new_states.append(new_state)

    return new_states

# Function to check if a state is the goal state
def is_goal(state):
    return state == goal_state

# Breadth-First Search (BFS)
def bfs(initial_state):
    queue = deque()
    visited = set()

    queue.append((initial_state, []))  # (state, path)

    while queue:
        current_state, path = queue.popleft()
        visited.add(tuple(map(tuple, current_state)))  # Convert to hashable format

        if is_goal(current_state):
            return path

        for new_state in generate_states(current_state):
            if tuple(map(tuple, new_state)) not in visited:
                queue.append((new_state, path + [new_state]))

    return None

# Solve the 8-puzzle
solution = bfs(initial_state)

if solution:
    print("Solution found:")
    for step, state in enumerate(solution):
        print(f"Step {step + 1}:")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
