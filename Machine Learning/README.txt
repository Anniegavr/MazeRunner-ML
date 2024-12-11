=== INTRODUCTION ===

The main goal of this side of the project is to develope Machine Learning agents who will proceed through different mazes and collect data based on their performances.
After some researching found out the optimal ML agent methods to accomplish the task, they are:
1. Q_learning 
2. Actor-Critic
3. DQL (Deep Q_learning)
4. DAC (Deep Actor-Critic)
5. A3C (Asynchronous Advantage Actor-Critic)
6. AlphaZero (Monte Carlo Tree Search + Deep RL) (Optional, because it’s for super complex environments)

During the course of the project should, or at least try, develope these agent methods. 

=== Main ===
This section will have consistent ideas, tasks, and updates based on the projet progress.

The data extraction points for the dataset are: 
1. Episodes = Number of episodes till the AI finds the best route
2. Maze Size = Ex: 31x31, 41x41
3. Maze type(optional) = Ex: Patrat, Dreptunghiular, Circular (Mai vedem de care)
4. Branching factor =  The average number of options (or paths) available per cell. Higher branching means more choices at each step, which could increase complexity.
5. Distance = Solution path length
6. Maze symmetry = the degree of mirroring or repetition in the structure of the maze
7. Dead Ends = the amount of dead ends per maze
8. Maze Density = how "full" or "cluttered" a maze is with walls compared to open valid spaces
9. Success rate = if the agent can make it in the offered number of episodes

Q_Learning.py UPDATE:
  The file now has the option to take the maze as input in the __main__ and you can get the agent's performances
  results as output.
  Mazes were created locally, they will be uploaded later on. 

