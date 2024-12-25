import os
import heapq
from typing import List, Tuple

def md(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def parse_maze(maze: List[str]) -> Tuple[Tuple[int, int], Tuple[int, int], List[List[str]]]:
    start, end = None, None
    grid = [list(row) for row in maze]
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)
    return start, end, grid

def neighbors(pos: Tuple[int, int], grid: List[List[str]]) -> List[Tuple[int, int]]:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    result = []
    for d in directions:
        ni, nj = pos[0] + d[0], pos[1] + d[1]
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
            result.append((ni, nj))
    return result

def a_star(grid: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: md(start, end)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in neighbors(current, grid):
            if grid[neighbor[0]][neighbor[1]] == '#':
                continue
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + md(neighbor, end)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []

def transform_maze(grid: List[List[str]], path: List[Tuple[int, int]]) -> List[List[str]]:
    for i, j in path[1:-1]:  # Exclude the first and last cell
        grid[i][j] = '.'
    return grid


# All existing functions (parse_maze, heuristic, neighbors, a_star, transform_maze) remain unchanged.

def process_mazes(directory: str, output_directory: str):
    """
    Processes all maze files in a given directory to ensure they have valid paths.
    
    Args:
        directory (str): Path to the directory containing maze files.
        output_directory (str): Path to save transformed mazes.
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if not filename.endswith('.txt'):  # Assume mazes are stored as .txt files.
            continue

        print(f"Processing: {filename}")
        with open(file_path, 'r') as file:
            maze = file.read().splitlines()

        start, end, grid = parse_maze(maze)
        if not start or not end:
            print(f"{filename}: Maze must have start (S) and end (E). Skipping...")
            continue

        path = a_star(grid, start, end)
        if not path:
            print(f"{filename}: No valid path found, transforming the maze.")
            path = a_star([[cell if cell != '#' else '.' for cell in row] for row in grid], start, end)
            grid = transform_maze(grid, path)

        if path:
            print(f"{filename}: Path found.")
        else:
            print(f"{filename}: No path possible even after transformation.")
        
        # Save the modified maze
        output_path = os.path.join(output_directory, filename)
        with open(output_path, 'w') as output_file:
            for row in grid:
                output_file.write(''.join(row) + '\n')

