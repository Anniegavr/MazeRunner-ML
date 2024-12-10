import numpy as np
import random
import sys
import os
from utils import utils
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils')) #just in case

from utils.maze import Maze

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
    optimal_path = a_star(self.maze) #Calculate the optimal path using A*
    epsilon_decay = 0.995 #Decay factor for epsilon/less exploration over time
    ipsilon_min = 1 #Minimum value for epsilon
    
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
        


        
          
    

