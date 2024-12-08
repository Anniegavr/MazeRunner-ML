import random
import numpy as np
import os
from utils.utils import md

MIN_SIZE = 11
MAX_SIZE = 31

MAX_MAZES = 150

def optimal_distance(width, height):
    max_distance = (width - 1) + (height - 1)
    return int(max_distance * random.uniform(0.4, 0.6))

def generate_mazes(max_mazes, output_folder="mazes"):
    #Ensure output directory exists
    os.makedirs(output_folder, exist_ok=True) 
    
    #Maze generation function for each maze in the loop
    def gerate_single_maze(width, height):
        maze = np.ones((height, width), dtype = int)
        
        #Starting point at a random location
        start_x, start_y = random.choice(range(1, width, 2)), random.choice(range(1, height, 2))
        maze[start_x, start_y] = 0 
        
        #Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures
        #Setting up the DFS Traversal
        stack  =[(start_x, start_y)]
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)] # Up, Down, Left, Right
        #The directions use a step of 2 to skip over walls and create pathways

        while stack:
            x, y = stack[-1]
            random.shuffle(directions)
            found = False
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 1 <= nx < width - 1 and 1 <= ny < height - 1 and maze[ny, nx] == 1:
                    maze[y + dy // 2, x + dx //2] = 0
                    maze[ny, nx] = 0
                    stack.append((nx, ny))
                    found = True
                    break
                if not found:
                    stack.pop()
        
        return maze, (start_x, start_y)
    
    #Create mazes for random sizes
    maze_counter = 0
    for _ in range(MAX_MAZES):
        #Randomly choose a width and height (both odd numbers between MIN_SIZE and MAX_SIZE)
        width = random.randrange(MIN_SIZE, MAX_SIZE + 1, 2) #Ensures odd numbers
        height = random.randrange(MIN_SIZE, MAX_SIZE + 1, 2) #Ensures odd numbers
    
        maze, start = gerate_single_maze(width, height)

        #Calculate optimal distance between start and exit based on maze size
        distance = optimal_distance(width, height)

        #Randomly select exit point ensuring minimum distance from start
        max_attemps = 100 #Limit the number of attemps to find a valid exit
        attemps = 0
        while attemps < max_attemps:
            exit_x, exit_y = random.choice(range(1, width, 2)), random.choice(range(1, height, 2))
            if maze[exit_x, exit_y] == 0 and md((start[0], start[1]), (exit_x, exit_y)) >= distance:
                break
            attemps += 1

        # If no valid exit is found after max_attemps, skip the maze
        if attemps == max_attemps:
            print(f"Warning: Maze {maze_counter + 1} failed to find a valid exit after {max_attemps} attemps")
            continue

        #Mark start and exit on the maze
        maze_filename = os.path.join(output_folder, f"maze_{width}x{height}_{maze_counter + 1}.txt")
        with open(maze_filename, "w") as f:
            for y, row in enumerate(maze):
                line = ""
                for x, cell in enumerate(row):
                    if (x, y) == (start[0], start[1]):
                        line += "S"
                    elif (x, y) == (exit_x, exit_y):
                        line += "E"
                    else:
                        line += "." if cell == 0 else "#"
                f.write(line + "\n")

        maze_counter += 1 

#main
generate_mazes(MAX_MAZES)
        
        


