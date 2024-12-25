## Installation
1. Install PyCharm or VSCode, although the recommended IDE is PyCharm.
2. Clone the repository and load it as a project in your IDE.
3. Ensure you also install an engine to run Jupyter Notebooks. Options: Anaconda or embedded Jupyter Notebook engine (for PyCharm).
4. Whether you want to generate mazes yourself, or to train agents on the generated mazes, or to check on the data analysis 
on how the agents performed, see the "Run the project" section below.

## Run the project
Read instructions.txt

## Project Description

The main goal of this side of the project is to develop Machine Learning agents who will proceed through different mazes and collect
data based on their performances. In real life, this project serves as the bases for robots who will navigate in environments
that constantly change their layouts or which are completely unknown to the humans, such as buildings, caves, markets.
After some researching found out the optimal ML agent methods to accomplish the task, they are:
1. Q_learning 
2. Actor-Critic
3. DQL (Deep Q_learning)
4. DAC (Deep Actor-Critic)
5. A3C (Asynchronous Advantage Actor-Critic)
6. AlphaZero (Monte Carlo Tree Search + Deep RL) (Optional, because it’s for super complex environments)

### Maze
The mazes are created by three main algorithms: DFS(Depth first Search), Binary Tree, Aldous-Broder. 
Each has its maze generation structure and can represent different environment in real life.

## AI Features

### Q-Learning
For training and for data extraction we used 3 different settings for the Q-Learning agent where the learning_rate and epsilon is the difference.
Determinative: lr = 0.3 epsilon = 0.3
Student: lr = 0.5 epsilon = 0.1
Explorer: lr = 0.1 epsilon = 0.5

### Predictions
At the end of the Exploratory Data Analysis, there is a section for predicting how the agents will do in random mazes. This shall help predicting if it is
worth training an agent on a maze before getting on with it, as it may take hours and might yield no result sometimes.

## Main

The data extraction points for the dataset are: 
1. Episodes = Number of episodes till the AI finds the best route
2. Maze Size = Ex: 31x31, 41x41
3. Maze type = Horizontal or Vertical
4. Distance = Solution path length
5. Maze symmetry = the degree of mirroring or repetition in the structure of the maze
6. Dead Ends = the amount of dead ends per maze
7. Maze Density = how "full" or "cluttered" a maze is with walls compared to open valid spaces
8. Success rate = if the agent can make it in the offered number of episodes
9. AgentType = Determinative, Student, Explorer
10. Algorithm = DFS, BinaryTree, Aldous-Broder

## How does this work?
The project can be divided in 3 sub-projects:
1. Maze generation
2. Agents training in maze-solving
3. Exploratory data analysis on how the agents perform in different mazes.

When generating mazes, they are saved in Machine Learning/mazes.
When training agents, the results are saved in Machine Learning/maze_results.csv.
When doing EDA, the generated csv is automatically found and used by the Jupyter Notebook located in the EDA folder.
