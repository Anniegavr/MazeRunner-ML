import numpy as np

def branching_factor(maze):
    rows, cols = maze.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    total_branches = 0
    open_cells = 0

    for x in range(rows):
        for y in range(cols):
            if maze[x, y] == 0:  # Check for open path
                open_cells += 1
                branches = 0
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and maze[nx, ny] == 0:
                        branches += 1
                total_branches += branches

    return total_branches / open_cells if open_cells else 0

def obstruction_density(maze):
    total_cells = maze.size
    wall_count = np.sum(maze == 1)  # Count cells with walls (#)
    return wall_count / total_cells

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
                if open_neighbors == 1:  # Dead end
                    dead_ends += 1
  return dead_ends

def symmetry(maze):
  rows = len(maze)
  cols = len(maze[0])

  # Calculate Vertical Symmetry
  vertical_symmetry_count = 0
  for i in range(rows):
    if cols % 2 == 0:
      left_half = maze[i][:cols // 2]
      right_half = maze[i][cols // 2:]
    else:
      left_half = maze[i][:cols // 2]
      right_half = maze[i][cols // 2 + 1:] #Skip the middle line
    if np.array_equal(left_half, right_half):
      vertical_symmetry_count += 1
    vertical_symmetry = vertical_symmetry_count / rows
   
  # Calculate Horizontal Symmetry
    horizontal_symmetry_count = 0
    for j in range(cols):
        if rows % 2 == 0:
            top_half = [maze[i][j] for i in range(rows // 2)]
            bottom_half = [maze[i][j] for i in range(rows // 2, rows)]
        else:
            top_half = [maze[i][j] for i in range(rows // 2)]
            bottom_half = [maze[i][j] for i in range(rows // 2 + 1, rows)] # Skip the middle row
        if top_half == bottom_half:
            horizontal_symmetry_count += 1
    horizontal_symmetry = horizontal_symmetry_count / cols

    # Calculate Overall Symmetry (average of vertical and horizontal symmetries)
    overall_symmetry = (vertical_symmetry + horizontal_symmetry) / 2
    return overall_symmetry
      
    
  
