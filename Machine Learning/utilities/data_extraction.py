import numpy as np


def dead_end(maze):
  rows, cols = maze.shape
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  dead_ends = 0

  for x in range(rows):
        for y in range(cols):
            if maze[x, y] == 0:  # Open path
                open_neighbors = sum(
                    1 for dx, dy in directions if 0 <= x+dx < rows and 0 <= y+dy < cols and maze[x+dx, y+dy] == 0
                )
                # If a cell has only one neighbor, it is a dead end
                if open_neighbors == 1:  
                    dead_ends += 1
  return dead_ends

def symmetry(maze):
    # Get the number of rows and columns in the maze
    rows = len(maze)
    cols = len(maze[0])

    # Calculate Vertical Symmetry
    vertical_symmetry_count = 0  
    for i in range(rows):
        # Split the current row into left and right halves
        if cols % 2 == 0:
            left_half = maze[i][:cols // 2]  # Left half of the row
            right_half = maze[i][cols // 2:]  # Right half of the row
        else:
            left_half = maze[i][:cols // 2]  # Left half (excluding middle column)
            right_half = maze[i][cols // 2 + 1:]  # Right half (excluding middle column)

        # Check if the left and right halves are equal (i.e., the row is vertically symmetric)
        if np.array_equal(left_half, right_half):
            vertical_symmetry_count += 1  # If they are equal, increment the count

    # Calculate the ratio of rows with vertical symmetry
    vertical_symmetry = vertical_symmetry_count / rows

    # Calculate Horizontal Symmetry
    horizontal_symmetry_count = 0  
    for j in range(cols):
        # Split the current column into top and bottom halves
        if rows % 2 == 0:
            # If the number of rows is even, split into equal halves
            top_half = [maze[i][j] for i in range(rows // 2)]  # Top half of the column
            bottom_half = [maze[i][j] for i in range(rows // 2, rows)]  # Bottom half of the column
        else:
            # If the number of rows is odd, skip the middle row
            top_half = [maze[i][j] for i in range(rows // 2)]  # Top half of the column
            bottom_half = [maze[i][j] for i in range(rows // 2 + 1, rows)]  # Bottom half of the column

        # Check if the top and bottom halves of the column are equal (i.e., the column is horizontally symmetric)
        if top_half == bottom_half:
            horizontal_symmetry_count += 1  # If they are equal, increment the count

    # Calculate the ratio of columns with horizontal symmetry
    horizontal_symmetry = horizontal_symmetry_count / cols

    # Calculate the Overall Symmetry by averaging the vertical and horizontal symmetries
    overall_symmetry = (vertical_symmetry + horizontal_symmetry) / 2

    return overall_symmetry

def density(maze):
    total_cells = maze.size
    wall_count = np.sum(maze == 1)  # Count cells with walls (#)
    return wall_count / total_cells
      
    
  