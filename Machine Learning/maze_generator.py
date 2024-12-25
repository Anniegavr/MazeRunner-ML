import random
import numpy as np
import os
from utilities.utils import md
from utilities.maze_fixer import process_mazes

MIN_SIZE = 11
MAX_SIZE = 31
OUTPUT_FOLDER = "Machine Learning/mazes"  # Save maze folder inside the 'Machine Learning' folder

#Depth First Search Algorithm
def generate_maze_dfs(width, height):
    maze = np.ones((height, width), dtype=int)
    start_x, start_y = random.choice(range(1, width, 2)), random.choice(range(1, height, 2))
    maze[start_y, start_x] = 0
    stack = [(start_x, start_y)]
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    while stack:
        x, y = stack[-1]
        random.shuffle(directions)
        found = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width - 1 and 1 <= ny < height - 1 and maze[ny, nx] == 1:
                maze[y + dy // 2, x + dx // 2] = 0
                maze[ny, nx] = 0
                stack.append((nx, ny))
                found = True
                break
        if not found:
            stack.pop()
    return maze, (start_x, start_y)

# Binary Tree Algorithm
def generate_maze_binary_tree(width, height):
    # Initialize maze with walls
    maze = np.ones((height, width), dtype=int)
    
    # Carve out the grid structure
    for y in range(1, height, 2):
        for x in range(1, width, 2):
            maze[y, x] = 0  # Open cell
            if y > 1 and random.choice([True, False]):
                maze[y - 1, x] = 0  # Carve upward
            elif x > 1:
                maze[y, x - 1] = 0  # Carve left
    start = (random.choice(range(1, width, 2)), random.choice(range(1, height, 2)))
    return maze, start

# Aldous-Broder Algorithm    
def generate_maze_aldous_broder(width, height):
    maze = np.ones((height, width), dtype=int)
    x, y = random.randrange(1, width, 2), random.randrange(1, height, 2)
    maze[y, x] = 0
    visited = {(x, y)}
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    while len(visited) < (width // 2) * (height // 2):
        dx, dy = random.choice(directions)
        nx, ny = x + dx, y + dy
        if 1 <= nx < width - 1 and 1 <= ny < height - 1:
            if (nx, ny) not in visited:
                maze[y + dy // 2, x + dx // 2] = 0
                maze[ny, nx] = 0
                visited.add((nx, ny))
            x, y = nx, ny
    return maze, (x, y)

# The function to calculate the distance between S and E based on maze size
def optimal_distance(width, height):
    max_distance = (width - 1) + (height - 1)
    return int(max_distance * 0.3)

# Function to save maze to file with start (S) and exit (E) points
def save_maze(maze, start, exit, filename):
    with open(filename, "w") as f:
        for y, row in enumerate(maze):
            line = ""
            for x, cell in enumerate(row):
                if (y, x) == (start[1], start[0]):  # Start point
                    line += "S"
                elif (y, x) == (exit[1], exit[0]):  # Exit point
                    line += "E"
                else:
                    line += "." if cell == 0 else "#"
            f.write(line + "\n")  

def generate_and_save_mazes(output_folder=OUTPUT_FOLDER):
    os.makedirs(output_folder, exist_ok=True)  # Ensure the folder is created
    algorithms = [
        ("DFS", generate_maze_dfs),
        ("BinaryTree", generate_maze_binary_tree),
        ("AldousBroder", generate_maze_aldous_broder),
    ]
    
    # Main iteration for maze generation
    for width in range(MIN_SIZE, MAX_SIZE + 1, 2):
        for height in range(MIN_SIZE, MAX_SIZE + 1, 2):
            for name, algorithm in algorithms:
                for i in range(3):  # Generate 3 mazes per size and algorithm
                    maze, start = algorithm(width, height)
                    distance = optimal_distance(width, height)
                    
                    # In 100 attempts try and find the optimal distance before creating the maze
                    max_attempts = 100  
                    attempts = 0
                    while attempts < max_attempts:
                        exit = (random.choice(range(1, width, 2)), random.choice(range(1, height, 2)))
                        if maze[exit[1], exit[0]] == 0 and md((start[0], start[1]), (exit[0], exit[1])) >= distance:
                            break
                        attempts += 1
                    
                    # If no valid exit is found after max_attempts, skip this maze
                    if attempts == max_attempts:
                        print(f"Warning: Maze failed to find optimal distance after {max_attempts} attempts.")
                        continue

                    # Save the maze
                    filename = os.path.join(output_folder, f"{width}x{height}_{name}_{i+1}.txt")
                    save_maze(maze, start, exit, filename)
                    # print(f"Saved {filename}")

generate_and_save_mazes()
# Ensure valid path
process_mazes("Machine Learning/mazes", "Machine Learning/mazes")
