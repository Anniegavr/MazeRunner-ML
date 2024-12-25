import pygame
import sys

pygame.init()

pygame.display.set_caption('Mazer')
# Variables defining the resolution of the window named "Mazer"
width = int(input())
height = int(input())

maze = [
["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
["#",".",".",".",".",".",".",".",".",".",".",".","#",".",".",".",".",".","#",".",".",".",".",".",".",".","#",".",".",".","#"],
["#",".","#","#","#","#","#",".","#","#","#","#","#",".","#","#","#",".","#",".","#",".","#","#","#",".","#",".","#",".","#"],
["#",".",".",".",".",".","#",".","#",".",".",".",".",".","#",".","#",".",".",".","#",".",".",".","#",".","#",".","#",".","#"],
["#",".","#","#","#",".","#",".","#",".","#","#","#","#","#",".","#","#","#","#","#","#","#",".","#",".","#",".","#",".","#"],
["#",".",".",".","#",".","#",".","#",".","#",".",".",".","#",".",".",".","#",".",".",".",".",".","#","S",".",".","#",".","#"],
["#",".","#","#","#",".","#",".","#",".","#",".","#",".","#",".","#",".","#",".","#","#","#","#","#","#","#","#","#",".","#"],
["#",".","#",".",".",".","#",".","#",".",".",".","#",".","#",".","#",".","#",".",".",".","#",".",".",".","#",".",".",".","#"],
["#",".","#",".","#","#","#","#","#","#","#","#","#",".","#",".","#",".","#","#","#",".","#",".","#",".","#",".","#","#","#"],
["#",".","#",".",".",".",".",".",".",".",".",".",".",".","#",".","#",".",".",".","#",".","#",".","#",".","#",".","#",".","#"],
["#",".","#","#","#","#","#","#","#","#","#","#","#","#","#",".","#","#","#","#","#",".","#",".","#","#","#",".","#",".","#"],
["#",".",".",".","#",".",".",".",".",".","#",".",".",".",".",".",".",".","#",".",".",".","#",".",".",".",".",".","#",".","#"],
["#","#","#",".","#",".","#","#","#",".","#","#","#","#","#",".","#",".","#",".","#","#","#","#","#",".","#","#","#",".","#"],
["#",".",".",".","#",".","#",".",".",".",".",".",".",".","#","E","#",".","#",".",".",".",".",".","#",".","#",".",".",".","#"],
["#",".","#","#","#",".","#","#","#","#","#","#","#",".","#","#","#",".","#","#","#","#","#",".","#",".","#",".","#",".","#"],
["#",".",".",".","#",".","#",".",".",".","#",".",".",".",".",".",".",".","#",".",".",".",".",".","#",".",".",".","#",".","#"],
["#","#","#",".","#",".","#",".","#",".","#","#","#","#","#","#","#",".","#",".","#","#","#","#","#","#","#","#","#",".","#"],
["#",".",".",".","#",".",".",".","#",".",".",".","#",".","#",".",".",".","#",".","#",".",".",".",".",".",".",".","#",".","#"],
["#",".","#","#","#","#","#","#","#","#","#",".","#",".","#",".","#","#","#",".","#",".","#","#","#","#","#",".","#",".","#"],
["#",".","#",".",".",".",".",".","#",".",".",".","#",".",".",".","#",".","#",".","#",".","#",".",".",".","#",".","#",".","#"],
["#",".","#","#","#",".","#",".","#",".","#","#","#","#","#",".","#",".","#",".","#",".","#",".","#",".","#",".","#",".","#"],
["#",".",".",".","#",".","#",".",".",".","#",".",".",".","#",".",".",".","#",".","#",".",".",".","#",".","#",".","#",".","#"],
["#","#","#",".","#",".","#","#","#","#","#",".","#",".","#","#","#","#","#",".","#","#","#","#","#","#","#",".","#",".","#"],
["#",".","#",".","#",".","#",".",".",".",".",".","#",".",".",".",".",".","#",".",".",".",".",".",".",".","#",".","#",".","#"],
["#",".","#",".","#",".","#",".","#","#","#","#","#","#","#","#","#",".","#","#","#","#","#","#","#",".","#",".","#",".","#"],
["#",".",".",".","#",".",".",".","#",".",".",".",".",".",".",".",".",".","#",".",".",".",".",".",".",".","#",".","#",".","#"],
["#",".","#","#","#","#","#","#","#",".","#","#","#","#","#","#","#",".","#",".","#","#","#","#","#","#","#",".","#",".","#"],
["#",".","#",".",".",".",".",".","#",".","#",".","#",".",".",".",".",".","#",".","#",".",".",".",".",".","#",".",".",".","#"],
["#",".","#",".","#","#","#",".","#",".","#",".","#","#","#","#","#","#","#",".","#",".","#","#","#","#","#",".","#","#","#"],
["#",".",".",".","#",".",".",".",".",".","#",".",".",".",".",".",".",".",".",".","#",".",".",".",".",".",".",".",".",".","#"],
["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
]
# Define the main surface/window with white color
screen = pygame.display.set_mode((width, height))
screen.fill('White')
# Define the clock variable to control frames per second (FPS)
clock = pygame.time.Clock()

while True:
    # Block of code that allows closing the "Mazer" Python window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit("Session Closed")
    # Loop that translates the maze variable into colors on the screen
    for index_column, columns in enumerate(maze):
        for index_row, rows in enumerate(maze[index_column]):
            # Variable determining the height of each colored rectangle representing elements such as walls ("#"), start ("S"), exit ("E"), and model position ("P")
            height_element = height / len(maze)
            # Variable determining the width of the mentioned rectangles
            width_element = width / len(maze[len(maze)-1])
            # List storing the current position of the model
            P = [index_column, index_row]
            # Block of code translating "#" as stable black rectangles
            if maze[index_column][index_row] == "#":
                # Variable (expressed as a non-main surface) storing the color corresponding to the element in the maze variable
                displayed_element = pygame.Surface((width_element, height_element))
                # Function that defines the color
                displayed_element.fill("Black")
                # Function that places the non-main surface displayed_element on the main surface screen
                screen.blit(displayed_element, ((index_row * width_element), (index_column * height_element)))
            # Block of code translating "S" as an unstable red rectangle, capable of turning blue when the model is just starting
            if maze[index_column][index_row] == "S":
                S = [index_column, index_row]
                displayed_element = pygame.Surface((width_element, height_element))
                if P[0:2] == S[0:2]:
                    displayed_element.fill("Blue")
                else:
                    displayed_element.fill("Red")
                screen.blit(displayed_element, ((index_row * width_element), (index_column * height_element)))
            # Block of code defining "E" as a stable green rectangle
            if maze[index_column][index_row] == "E":
                E = [index_column, index_row]
                displayed_element = pygame.Surface((width_element, height_element))
                if P[0:2] == E[0:2]:
                    sys.exit("Exit Achieved")
                displayed_element.fill("Green")
                screen.blit(displayed_element, ((index_row * width_element), (index_column * height_element)))
            # Defines the position where "P" is as a blue rectangle
            if maze[index_column][index_row] == "P":
                displayed_element = pygame.Surface((width_element, height_element))
                displayed_element.fill("Blue")
                screen.blit(displayed_element, ((index_row * width_element), (index_column * height_element)))
            # Ensures empty spaces are white
            if maze[index_column][index_row] not in ["P", "S", "E", "#"]:
                displayed_element = pygame.Surface((width_element, height_element))
                displayed_element.fill("White")
                screen.blit(displayed_element, ((index_row * width_element), (index_column * height_element)))
            # Block of code creating the loop to return to the starting point if failing to reach "E"
            if maze[P[0]:P[1]] == "#":
                P[0:2] = S[0:2]
                maze[S[0], S[1]] = "P"
    # Ensures the image updates with every frame
    pygame.display.update()
    # Sets the FPS to 30
    clock.tick(30)
