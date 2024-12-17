import numpy as np
import heapq
from utilities.maze import Maze

def md(a,b):
    #Manhattan Distance or heuristic = |x1 - x2| + |y1 - y2|
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

#Open and read maze file function
def load_maze(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    maze_date = []
    start = None
    exit = None

    for y , line in enumerate(lines):
        row = []
        for x, char in enumerate(line.strip()): 
            if char == "S":
                start = (x, y)
                row.append(0)
            elif char == "E":
                exit = (x, y)
                row.append(0)
            elif char == "#":
                row.append(1) #wall
            elif char == ".":
                row.append(0) #path
        maze_data.append(row)

   #Convert maze data to a numpy array
   maze_data = np.array(maze_data)
   return maze_data, start, exit

#Calculate the shortest path function A*
def a_star(maze):
    start = maze.start #Starting point (S)
    exit = maze.exit #Exit point (E) 

    #Ensure the start and exit are valid positions
    if maze.grid[start[0]][start[1]] == 1 or maze.grid[exit[0]][exit[1]] == 1:
        raise ValueError("Start or exit position are inside walls")
        
    #Initialize the open and closed lists, and other nnecesary data structures 
    open_list = [] #Contains nodes to be evaluated (initially just the start node).
    closed_list = set() #Contains nodes that have already been evaluated.
    came_from = {} #To track the path
    g_score = {start: 0} #Cost from start to current position
    f_score = {start: md(start, exit)} #Estimated cost to goal(calculated with manhattan distance function)

    heapq.heappush(open_list, (f_score[start], start)) #Push start position to open list

    while open_list: #while open_list is not empty
        current_f, current = heapq.heappop(open_list) #Get the node with the lowest f score

        #If we reach the exit, reconstruct the path
        if current == exit:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start) # Add the start position to the path
            path.reverse() #Reverse the path to get it from the start to exit
            path = path[:-1] #Exclude the exit from the path
            return path
        
        closed_list.add(current)

        #Check the 4 possible movements (Up, Down, Left, Right)
        for action in range(4):
            x, y = current
            movements = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            dx, dy = movements[actions]
            nex_x, new_ y = x + dx, y + dy

            #Check if the next state is a valid one, within bounds and not a wall
            if 0 <= new_x < len(maze.grid[0]) and 0 <= new_y < len(maze.grid):
                if maze.grid[nex_x][new_y] == 0: #Walkable space
                    next_state = (next_x, next_y)
                else:
                    continue #Skip if the next state is a a wall
            else:
                continue #Skip if out of bounds

            if next_state in closed_list: #Ignore if the state has already been visited
                continue

            #Calculate the tentative g score(cost to move to the next state)
            tentative_g_score = g_score.get(current, float("inf")) + 1 # Each step costs 1
            
            #If this path to the next state is better, update it
            if next_state not in g_score or tentative_g_score < g_score[next_state]:
                came_from[next_state] = current
                g_score[next_state] = tentative_g_score
                f_score[next_state] = g_score[next_state] + md(next_state, exit) # f = g + h
                heapq.heappush(open_list, (f_score[next_state], next_state)) # Add to opne list

    return [] # No valid pathfound
        
        
        
        






   
