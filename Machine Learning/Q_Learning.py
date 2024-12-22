import numpy as np
import random
import sys
import os
from utils import utils
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils')) #just in case

from utils.maze import Maze
from utils import data_extraction

class QLearningAgent:
  def __init__(self, maze, learning_rate=0.1, discount_factor=0.9, epsilon=0.2):
    self.maze = maze #The maze environment
    self.learning_rate = learning_rate #The learning rate (alpha)
    self.discount_factor = discount_factor #The discount factor (gamma)
    self.epsilon = epsilon #The exploration factor (epsilon)
    self.q_table = np.random.uniform(low=-1, high=1, size=(maze.grid.shape[0], maze.grid.shape[1], 4))
    self.solution_path = [] #To store the final solution path
    self.episode_taken = 0 #TO store the number of episodes taken
  
  def train(self, num_episodes):
    optimal_path = utils.a_star(self.maze) #Calculate the optimal path using A*
    epsilon_decay = 0.995 #Decay factor for epsilon/less exploration over time
    epsilon_min = 1 #Minimum value for epsilon
    
    for episode in range(num_episodes):
      state = self.maze.start
      done = False
      ai_path = [] #List to store the AI's path in the current episode.
      
      while not done:
        if random.uniform(0, 1) < self.epsilon:
          action = random.choise([0, 1, 2, 3]) #Exploration
        else:
          action = np.argmax(self.q_table[state[1], state[0]]) # Explotation
        
        next_state, reward, done = self.maze.step(state, action)

        ai_path.append(state)
        
        best_next_action = np.argmax(self.q_table[next_state[1], next_state[0]])
        #Main formula for Q_Learning, action-value greedy policy, Q(st​,at​)=Q(st​,at​)+α[rt+1​+γa′max​Q(st+1​,a′)−Q(st​,at​)]
        self.q_table[state[1], state[0], action] = (self.q_table[state[1], state[0], action] + 
                                                   self.learning_rate * (reward + self.discount_factor * self.q_table[next_state[1], next_state[0], best_next_action] - self.q_table[state[1], state[0], action]))
        
        state = next_state

      self.episodes_taken += 1
      self.epsilon = max(self.epsilon * epsilon_decay, epsilon_min) #Less exploration over time
 
      if ai_path == optimal_path:
        #print(f"AI found the optimal path in episode {episode + 1}!")
        break
        
  def report_metrics(self):
    #Training data and extraction data results
    maze_size = self.maze.grid.shape #Rows and columns
    branching = data_extraction.branching_factor(self.maze.grid)
    density = data_extraction.onstruction_density(self.maze.grid)
    sym = data_extraction.symmetry(self.maze.grid)
    dead_ends = data_extraction.dead_ends(self.maze.grid)
    solution_length = utils.md(self.maze.start, self.maze.exit)
    
    print("\n=== Maze Metrics ===")
    print(f"Size: {maze_size}")
    print(f"Branching Factor: {branching: .2f}")
    print(f"Density: {density: .2f}")
    print(f"Symmetry: {sym: .2f}")
    print(f"Dead ends: {dead_ends}")
    print(f"Solution Path Length: {solution_length}")

#Train agent and observe the results
if __name__ == "__main__":
  #Load the maze from a file
  maze_file = "mazes/maze_11x11_80.txt"
  maze_grid, start, exit = utils.load_maze(maze_file)
  
  #Initialize the Maze environment 
  maze = Maze(maze_grid, start, exit)
  
  num_runs = 1
  episode_results = [] #List to store the episodes count for each run

  for run in range(num_runs):
    #Initialize Q-learning agent
    agent = QLearningAgent(maze)
    
    #Train
    agent.train(num_episodes=1000)
    episode_results.append(agent.episodes_taken)
    
  #Report metrics after training
  print("\nFinal metrics after training:")
  agent.report_metrics()
  
  #Calculate and display the average episodes
  average_episodes = sum(episode_results) / len(episode_results)
  print(f"\n=== Average Results Over {num_runs} Runs ===")
  print(f"Average Episodes Taken: {int(average_episodes)}")

  
  
        
          
    

