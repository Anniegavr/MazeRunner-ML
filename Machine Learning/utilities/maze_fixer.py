"""

This file was created with the assistance of ChatGPT due to the instability encountered with Binary Tree mazes. 
While most of the functions below are similar to the existing ones in other files, attempts to refactor and implement 
certain changes to minimize code resulted in unexpected behavior. Despite trying to optimize, the new version failed to 
work as intended.

In the end, I chose to adhere to a fundamental programming principle:

=== If it works, don't touch it. ===

For now, this version is stable, and no further changes will be made unless absolutely necessary.

"""

import os
import heapq
from typing import List, Tuple

def md(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# Parses the maze to find start ('S'), end ('E'), and convert the maze into a grid
def parse_maze(maze: List[str]) -> Tuple[Tuple[int, int], Tuple[int, int], List[List[str]]]:
    start, end = None, None
    grid = [list(row) for row in maze]  # Convert each row of the maze into a list
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':  # Identify the start position
                start = (i, j)
            elif cell == 'E':  # Identify the end position
                end = (i, j)
    return start, end, grid

# Finds valid neighbors (up, down, left, right) for the current position in the grid
def neighbors(pos: Tuple[int, int], grid: List[List[str]]) -> List[Tuple[int, int]]:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Directional moves (right, down, left, up)
    result = []
    for d in directions:
        ni, nj = pos[0] + d[0], pos[1] + d[1]
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):  # Check if the neighbor is within bounds
            result.append((ni, nj))
    return result

# Implements the A* algorithm to find the shortest path from start to end in the maze
def a_star(grid: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
    open_set = [(0, start)]  # Priority queue storing (f_score, position)
    came_from = {}  # Tracks the parent of each node
    g_score = {start: 0}  # Cost to reach each node from the start
    f_score = {start: md(start, end)}  # Estimated total cost from start to end through each node

    while open_set:
        _, current = heapq.heappop(open_set)  # Get the node with the lowest f_score

        if current == end:  # If the end is reached, reconstruct the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return the path in correct order

        for neighbor in neighbors(current, grid):
            if grid[neighbor[0]][neighbor[1]] == '#':  # Skip walls
                continue
            tentative_g_score = g_score[current] + 1  # Cost to move to the neighbor
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current  # Update the parent
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + md(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))  # Push to the open set

    return []  # Return an empty path if no valid path is found

# Updates the maze grid with the path found (excluding start and end points)
def transform_maze(grid: List[List[str]], path: List[Tuple[int, int]]) -> List[List[str]]:
    for i, j in path[1:-1]:  # Exclude the first (start) and last (end) cells
        grid[i][j] = '.'  # Mark the path
    return grid

# Processes maze files in a given directory, finds paths, and saves modified mazes
def process_mazes(directory: str, output_directory: str):
    """
    Processes all maze files in a given directory to ensure they have valid paths.
    
    Args:
        directory (str): Path to the directory containing maze files.
        output_directory (str): Path to save transformed mazes.
    """
    if not os.path.exists(output_directory):  # Create the output directory if it doesn't exist
        os.makedirs(output_directory)
    
    for filename in os.listdir(directory):  # Iterate over all files in the directory
        file_path = os.path.join(directory, filename)
        if not filename.endswith('.txt'):  # Process only .txt files
            continue

        print(f"Processing: {filename}")
        with open(file_path, 'r') as file:
            maze = file.read().splitlines()  # Read the maze file into a list of strings

        start, end, grid = parse_maze(maze)
        if not start or not end:  # Skip mazes without valid start or end points
            print(f"{filename}: Maze must have start (S) and end (E). Skipping...")
            continue

        path = a_star(grid, start, end)  # Attempt to find a path using A*
        if not path:
            print(f"{filename}: No valid path found, transforming the maze.")
            # Replace walls with open cells and retry
            path = a_star([[cell if cell != '#' else '.' for cell in row] for row in grid], start, end)
            grid = transform_maze(grid, path)  # Mark the new path on the grid

        if path:
            print(f"{filename}: Path found.")
        else:
            print(f"{filename}: No path possible even after transformation.")
        
        # Save the modified maze to the output directory
        output_path = os.path.join(output_directory, filename)
        with open(output_path, 'w') as output_file:
            for row in grid:
                output_file.write(''.join(row) + '\n')  # Write the modified grid back to a file
