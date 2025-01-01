import os
import csv
import numpy as np
from concurrent.futures import ProcessPoolExecutor
from utilities.data_extraction import symmetry, dead_end, density
from utilities.maze import Maze
from Q_Learning import QLearningAgent
from utilities.utils import load_maze


def process_single_maze(filename, directory, num_runs, episode_limit, fieldnames, maze_type_mapping):
    """Process a single maze and return results for all agent types."""
    results = []

    # Parse ID and maze type from filename
    maze_id = filename.replace(".txt", "")
    maze_type = filename.split('_')[1]
    maze_id_abbr = maze_id.replace(maze_type, maze_type_mapping.get(maze_type, maze_type))

    # Determine orientation
    size_parts = filename.split('_')[0]
    width, height = map(int, size_parts.split('x'))
    orientation = "Square" if width == height else "Horizontal" if width > height else "Vertical"

    # Load the maze
    maze_path = os.path.join(directory, filename)
    maze_grid, start, exit = load_maze(maze_path)
    maze = Maze(maze_grid, start, exit)

    # Compute maze properties
    sym = symmetry(maze.grid)
    den = density(maze.grid)
    d_ends = dead_end(maze.grid)

    # Collect Q-Learning results for different agents
    agent_types = [
        ("Q-Determinative", 0.3, 0.3),
        ("Q-Student", 0.5, 0.1),
        ("Q-Explorer", 0.1, 0.5),
    ]

    for agent_type, learning_rate, epsilon in agent_types:
        episodes_results = []

        for run in range(num_runs):
            agent = QLearningAgent(maze, learning_rate=learning_rate, epsilon=epsilon)
            agent.train(num_episodes=episode_limit)

            episodes_results.append(agent.episodes_taken)
            spl = agent.solution_path_length()

        # Calculate averages
        avg_episodes = np.mean(episodes_results)

        # Prepare data for this result
        result = {
            "ID": maze_id_abbr,
            "Size": (width, height),
            "Maze Type": maze_type,
            "Orientation": orientation,
            "Agent Type": agent_type,
            "Symmetry": round(sym, 2),
            "Density": round(den, 2),
            "Dead Ends": d_ends,
            "Solution Path Length": int(spl),
            "Average Episodes": int(avg_episodes),
        }
        results.append(result)

    return results


def process_all_mazes(directory, output_file, num_runs, episode_limit):
    # Open the CSV file once and write the header
    fieldnames = ["ID", "Size", "Maze Type", "Orientation", "Agent Type", "Symmetry", "Density", "Dead Ends",
                  "Solution Path Length", "Average Episodes"]

    maze_type_mapping = {
        "DFS": "DFS",
        "BinaryTree": "BT",
        "AldousBroder": "AB"
    }

    maze_files = [f for f in sorted(os.listdir(directory)) if f.endswith(".txt")]

    # Use ProcessPoolExecutor for parallelism
    with ProcessPoolExecutor() as executor, open(output_file, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Submit each maze for processing
        futures = [
            executor.submit(process_single_maze, filename, directory, num_runs, episode_limit, fieldnames,
                            maze_type_mapping)
            for filename in maze_files
        ]

        for future in futures:
            # Write results as they are completed
            for result in future.result():
                writer.writerow(result)

            print(f"Processed maze: {result['ID']}")


# Main execution
if __name__ == "__main__":
    maze_directory = "Machine Learning/mazes"  # Directory containing the maze files
    output_csv = "Machine Learning/maze_results.csv"  # Full path to the CSV file (including folder and name)
    process_all_mazes(maze_directory, output_csv, num_runs=1, episode_limit=2500)
