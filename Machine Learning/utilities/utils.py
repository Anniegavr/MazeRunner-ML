import numpy as np
import heapq

def md(a, b):
    """Manhattan Distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def load_maze(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    maze_data = []
    start = None
    exit = None

    for y, line in enumerate(lines):
        row = []
        for x, char in enumerate(line.strip()):
            if char == "S":
                start = (x, y)
                row.append(0)
            elif char == "E":
                exit = (x, y)
                row.append(0)
            elif char == "#":
                row.append(1)  # wall
            elif char == ".":
                row.append(0)  # path
        maze_data.append(row)

    maze_data = np.array(maze_data)
    return maze_data, start, exit


def a_star(maze):
    start = maze.start  # Starting point (S)
    exit = maze.exit    # Exit point (E)

    # Ensure the start and exit are valid positions
    if maze.grid[start[1]][start[0]] == 1 or maze.grid[exit[1]][exit[0]] == 1:
        raise ValueError("Start or exit positions are inside walls.")
    
    # Initialize the open and closed lists, and other necessary data structures
    open_list = []
    closed_list = set()
    came_from = {}  # To track the path
    g_score = {start: 0}  # Cost from start to current position
    f_score = {start: md(start, exit)}  # Estimated cost to goal (heuristic)
    
    heapq.heappush(open_list, (f_score[start], start))  # Push start position to open list
    
    while open_list:
        current_f, current = heapq.heappop(open_list)  # Get the node with the lowest f score
        
        # If we reach the exit, reconstruct the path
        if current == exit:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)  # Add the start position to the path
            path.reverse()  # Reverse the path to get it from start to exit
            path = path[:-1]  # Exclude the exit position from the path
            return path  # Return the path excluding the exit position
        
        closed_list.add(current)
        
        # Check the 4 possible movements (Up, Down, Left, Right)
        for action in range(4):
            next_state = maze.valid_move(current, action)  # Get the next valid state based on the action
            
            if next_state in closed_list:  # Ignore if the state has already been visited
                continue
            
            # Ensure next_state is walkable
            x, y = next_state
            if maze.grid[y][x] == 1:  # Wall check
                continue
            
            # Calculate the tentative g score (cost to move to the next state)
            tentative_g_score = g_score.get(current, float('inf')) + 1  # Each step costs 1
            
            # If this path to the next state is better, update it
            if next_state not in g_score or tentative_g_score < g_score[next_state]:
                came_from[next_state] = current
                g_score[next_state] = tentative_g_score
                f_score[next_state] = g_score[next_state] + md(next_state, exit)  # f = g + h
                heapq.heappush(open_list, (f_score[next_state], next_state))  # Add to open list
    
    return []  # No valid path found



