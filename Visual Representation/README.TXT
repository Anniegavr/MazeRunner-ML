=== Note: Due to unexpected circumstances, this part of the project is not finished and does not fulfill all the planned features. ===          

# Maze Solver Visualization

This Python script is designed to visualize the process of solving a maze using Pygame, a library for building graphical applications. The visualization displays a grid-based maze on a blank canvas, with color-coded rectangles representing various elements. It dynamically translates each maze element into colors, which are immediately rendered on the canvas.

## Key Features

1. **Window Customization**:
   - Users provide two integers to specify the width and height of the visualization window, ensuring flexibility for different screen sizes.

2. **Color Mapping**:
   - **White**: Blank spaces (unoccupied grid cells).
   - **Black**: Obstacles or walls in the maze.
   - **Green**: The path taken by the model to traverse the maze.
   - **Blue**: The starting point of the maze.
   - **Red**: The exit point of the maze.

3. **Interactive Animation**:
   - The model's movement through the maze is visualized in real-time, with the frame rate capped at 30 FPS for stable performance.

4. **Collision Detection**:
   - If the model touches a black rectangle (wall), it resets to the starting position.
   - This feature simulates a penalty for invalid moves.

5. **Completion Handling**:
   - Upon reaching the exit (red rectangle), the application closes automatically, signaling the successful completion of the maze.

6. **Optimized Visualization**:
   - Efficient rendering ensures smooth operation, even for complex or larger mazes.

## How It Works

- The program reads a grid representation of the maze and translates it into rectangles on the canvas, with colors determined by specific "if" conditions.
- The model starts at the defined "start" position and progresses through the maze step-by-step.
- The frame rate ensures a consistent and visually comprehensible pace for observing the model's behavior.

## Usage Instructions

1. Install the required libraries (Pygame):
     pip install pygame (if not in requirements)
   

2. Run the script and provide the width and height of the window as prompted.

3. Observe the visualization as the model navigates through the maze.

4. Customize the maze representation or modify the code for different visual effects or algorithms.

## Ideal For

This script is ideal for understanding how pathfinding algorithms or decision-making processes navigate a maze, providing an engaging visual aid for learning or debugging.
