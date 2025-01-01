import random
import numpy as np
import os
from utilities.utils import md
from utilities.maze_fixer import process_mazes

MIN_SIZE = 11
MAX_SIZE = 31
OUTPUT_FOLDER = "Machine Learning/mazes"  # Where the maze folder and the mazes should be saved

# Depth First Search Algorithm
def generate_maze_dfs(width, height):
    maze = np.ones((height, width), dtype=int)
    start_x, start_y = random.choice(range(1, width, 2)), random.choice(range(1, height, 2))
    maze[start_y, start_x] = 0

    # Initialize the stack with the starting point (for DFS)
    stack = [(start_x, start_y)]
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    # Continue until the stack is empty (i.e., no more paths to explore)
    while stack:
        # Get the current position (x, y) from the stack
        x, y = stack[-1]
        random.shuffle(directions)

        found = False # A flag to check if a valid move was found

        # Try each direction from the current position
        for dx, dy in directions:
            # Calculate the new position (nx, ny)
            nx, ny = x + dx, y + dy

            # Check if the new position is within bounds and hasn't been visited yet (must be a wall)
            if 1 <= nx < width - 1 and 1 <= ny < height - 1 and maze[ny, nx] == 1:
                # Carve a path: set the wall between the current and new position to open space
                maze[y + dy // 2, x + dx // 2] = 0
                maze[ny, nx] = 0 # Set the new position as open

                # Push the new position to the stack to continue exploring from there
                stack.append((nx, ny))

                # Mark that we found a valid direction
                found = True
                break # Exit the loop as we have moved to a new position

        # If no valid direction was found (dead-end), pop the current position from the stack        
        if not found:
            stack.pop()
    return maze, (start_x, start_y)

# Binary Tree Algorithm
def generate_maze_binary_tree(width, height):
    maze = np.ones((height, width), dtype=int)
    
    # Loop through each cell in the grid, stepping by 2 to ensure we only consider odd-indexed cells
    for y in range(1, height, 2): # Iterate through odd rows
        for x in range(1, width, 2): # Iterate through odd columns
            maze[y, x] = 0  # Open the current cell (0 represents open space)

            # If we're not at the first row and randomly decide to carve upward
            if y > 1 and random.choice([True, False]):
                maze[y - 1, x] = 0  # Carve upward, making the cell above open

            # Otherwise, if we're not at the first column, carve left
            elif x > 1:
                maze[y, x - 1] = 0  # Carve left, making the cell to the left open

    start = (random.choice(range(1, width, 2)), random.choice(range(1, height, 2)))
    return maze, start

# Aldous-Broder Algorithm    
def generate_maze_aldous_broder(width, height):
    maze = np.ones((height, width), dtype=int)
    x, y = random.randrange(1, width, 2), random.randrange(1, height, 2)

    # Set the starting point as open space (0 represents empty space)
    maze[y, x] = 0
    # Keep track of visited cells in the maze (set to start with the initial point)
    visited = {(x, y)}
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    # Continue carving until we've visited a sufficient number of cells
    while len(visited) < (width // 2) * (height // 2):
        dx, dy = random.choice(directions)

        # Calculate the new position after moving
        nx, ny = x + dx, y + dy

        # Check if the new position is within the maze bounds
        if 1 <= nx < width - 1 and 1 <= ny < height - 1:
            # If the new position has not been visited before, carve a path
            if (nx, ny) not in visited:
                # Carve a path between the current and new position (set the wall between them to open space)
                maze[y + dy // 2, x + dx // 2] = 0
                maze[ny, nx] = 0

                # Add the new position to the visited set
                visited.add((nx, ny))

            #Move to the new position
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

def manually_create_maze(width, height, algorithm_name, start, exit):
    """
    Manually create a maze with specified parameters.

    Args:
        width (int): Width of the maze (must be an odd number).
        height (int): Height of the maze (must be an odd number).
        algorithm_name (str): Name of the maze generation algorithm ("DFS", "BinaryTree", "AldousBroder").
        start (tuple): Coordinates of the start point (x, y).
        exit (tuple): Coordinates of the exit point (x, y).

    Returns:
        None: Saves the maze to a file in the OUTPUT_FOLDER.
    """
    if width % 2 == 0 or height % 2 == 0:
        raise ValueError("Width and height must be odd numbers to generate a valid maze.")
    
    algorithms = {
        "DFS": generate_maze_dfs,
        "BinaryTree": generate_maze_binary_tree,
        "AldousBroder": generate_maze_aldous_broder,
    }
    
    if algorithm_name not in algorithms:
        raise ValueError(f"Invalid algorithm name. Choose from {list(algorithms.keys())}.")
    
    # Generate the maze using the selected algorithm
    algorithm = algorithms[algorithm_name]
    maze, generated_start = algorithm(width, height)
    
    # Validate start and exit points
    if maze[start[1], start[0]] != 0:
        raise ValueError("The specified start point is not on an open cell in the maze.")
    if maze[exit[1], exit[0]] != 0:
        raise ValueError("The specified exit point is not on an open cell in the maze.")
    
    # Save the manually created maze
    filename = os.path.join(OUTPUT_FOLDER, f"{width}x{height}_{algorithm_name}_manual.txt")
    save_maze(maze, start, exit, filename)
    print(f"Manually created maze saved as {filename}.")


def generate_and_save_mazes(output_folder=OUTPUT_FOLDER):
    os.makedirs(output_folder, exist_ok=True)  # Ensure the folder is created
    algorithms = [
        ("DFS", generate_maze_dfs),
        ("BinaryTree", generate_maze_binary_tree),
        ("AldousBroder", generate_maze_aldous_broder),
    ]
    
    # Main iteration for maze generation
    # Loop through each possible size (odd numbers for width and height to maintain the maze structure)
    for width in range(MIN_SIZE, MAX_SIZE + 1, 2): # Loop through odd widths
        for height in range(MIN_SIZE, MAX_SIZE + 1, 2): # Loop through odd heights
            for name, algorithm in algorithms: # Loop through each algorithm
                for i in range(3):  # Generate 3 mazes per size and algorithm

                    # Generate the maze using the selected algorithm
                    maze, start = algorithm(width, height)

                    # Calculate the optimal distance for the current maze size
                    distance = optimal_distance(width, height)
                    
                    # In 100 attempts try and find the optimal distance before creating the maze
                    max_attempts = 100  
                    attempts = 0
                    while attempts < max_attempts:
                        exit = (random.choice(range(1, width, 2)), random.choice(range(1, height, 2)))

                        # Check if the exit is valid (open space and distance criteria met)
                        if maze[exit[1], exit[0]] == 0 and md((start[0], start[1]), (exit[0], exit[1])) >= distance:
                            break # Valid exit found, break out of the loop
                        attempts += 1
                    
                    # If no valid exit is found after max_attempts, skip this maze
                    if attempts == max_attempts:
                        print(f"Warning: Maze failed to find optimal distance after {max_attempts} attempts.")
                        continue

                    # Save the maze
                    filename = os.path.join(output_folder, f"{width}x{height}_{name}_{i+1}.txt")
                    save_maze(maze, start, exit, filename)
                    # print(f"Saved {filename}")
                    

# manually_create_maze(41, 41, "DFS", (1, 1), (21, 21))
generate_and_save_mazes()
# Ensure valid path
process_mazes("Machine Learning/mazes", "Machine Learning/mazes")