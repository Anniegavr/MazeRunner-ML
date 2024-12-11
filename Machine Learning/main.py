import os
import csv
import numpy as np

from utils.utils import load_maze_from_file, a_star, md
from utils.data_extraction import branching_factor, obstruction_density, symmetry, dead_end
from utilities.maze import Maze
from Q_Learning import QLearningAgent

def procces_all_mazes(directory, output_file, num_runs=10, episode_limit=500):
  #List to store result
  results = []
  
  for filename in sorted(os.listdir(directory)):
    if filename.ednswith(".txt"):
        #Only the maze size and it's number as ID
        maze_id = filename.replace("maze_", "").replace(".txt", "")

    #Load the maze
    maze_path = os.path.join(directory, filename)
    maze_grid, start, exit = load_maze(maze_path)
    maze = Maze(maze_grid, start, exit)

    #CSV columns
    size = maze.grid.shape
    branching = branching_factor(maze.grid)
    density = obstruction_density(maze.grid)
    sym = symmetry(maze.grid)
    dead_ends = dead_end(maze.grid)
    solution_length = md(maze.start, maze.exit)

    # Collect Q-Learning results
    successful_runs = 0
    episodes_results = []
    
    for run in range(num_runs):
      agent = QLearningAgent(maze)
      agent.train(num_episodes=10000)
      
      #Check if the agent solved the maze within the episode limit
      if agent.episode_taken <= episode_limit:
        successful_runs +=1
        episodes_results.append(agent.episodes_taken)
    
    #Calculate averages success rate
    avg_episodes = np.mean(epsiode_results)
    success_rate = (success_runs / num_runs) * 100 #Convert to percentage
    
    #Add data to results
    results.append({
      "ID" : maze_id,
      "Size": size,
      "Branching Factor": round(branching, 2),
      "Density": round(density, 2),
      "Symmetry": round(sym, 2),
      "Dead Ends": dead_ends,
      "Solution Path Length": int(solution_length),
      "Average Episodes": int(avg_episodes),
      "Succes Rate (%)": round(success_rate, 2)
    })

    print(f"Processed: {filename} (ID: {maze_id})")
  
  #Write results to the CSV File
  with open(output_file), "w", newline="") as csvfile:
    fieldnames = ["ID", "Size", "Branching Factor", "Density", "Symmetry", "Dead Ends", 
                      "Solution Path Length", "Average Episodes", "Success Rate (%)"]
    writer = csv.DictWriter(csv, fieldnames=fieldnames)
    
    writer.writeheader()
    for result in results:
      writer.writerow(results)
      
  print(f"\nResults saved to {output_file}")

# Main
if __name__ == "__main__":
  maze_directory = "mazes"
  output_csv = "results.csv"
  precess_all_mazes(maze_directory, output_csv, num_runs=10, episode_limit=500 )






