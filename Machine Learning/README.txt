=== Run the project ===
Read instructions.txt

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

=== Project UPDATE === 
After finishing coding Deep Q-Learning agent and using mazes to train him we encountered a problem. First of all, the result met the expectations,
the agent was able to solve a 41x41 maze, the problem was it's speed. Compared to the regular Q-Learning, the Deep Q-Learning agent was finding the 
shortest path much slower. In this case we would not be able to extrat the necessary data for EDA before deadline.

After not so long we decided to change the strategy of the project. Instead of using multiple Machine Learning agents, we will focus only on the one
which we know it works perfectly, Q-Learning. We will expand it's possibilities to extract more relevant data and the mazes as well.

=== Maze ===
The mazes will be created by three main algorithms: DFS(Depth first Search), Binary Tree, Aldous-Broder. 
Each has it's maze generation structure and can represent different environment in real life.

=== Q-Learning ===
In trainning and for data extraction we will use 3 different settings for the Q-Learning agent where the learning_rate and epsilon is the difference.
Determinative: lr = 0.3 epsilon = 0.3
Stundent: lr = 0.5 epsilon = 0.1
Explorer: lr = 0.1 epsilon = 0.5

=== Main ===
This section will have consistent ideas, tasks, and updates based on the projet progress.

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