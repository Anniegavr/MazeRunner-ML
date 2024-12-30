# Maze Navigation with Machine Learning Agents

This project focuses on developing Machine Learning agents to navigate through various mazes and collect data on their performance. The insights gained can inform real-life applications such as robots navigating dynamic or unknown environments like buildings, caves, or markets.
Installation

Clone the Repository
Clone the project repository to your local machine:
 
    git clone https://github.com/Anniegavr/MazeRunner-ML.git

Create a Virtual Environment
Create a Python virtual environment to isolate dependencies:

python -m venv env

Activate the environment:

On Windows:

    .\env\Scripts\activate

On macOS/Linux:

    source env/bin/activate

Install Requirements
Install all required Python packages from requirements.txt:

    pip install -r requirements.txt

Set Up Jupyter Notebook
If you plan to perform Exploratory Data Analysis (EDA), install Jupyter Notebook:

    pip install notebook

Recommended IDE
For the best experience, use PyCharm, which provides integrated solutions for Python development and Jupyter Notebooks.

Run the Project
Step 1: Maze Generation
### Generate Mazes Automatically

   Open the maze_generator.py script.
   Set the desired minimum (MIN) and maximum (MAX) maze sizes in the script.
   Run the script to generate mazes within the specified size range.

Generate Mazes Manually

   Use the manually_create_maze() function in maze_generator.py.
   Example parameters:
        width: Width of the maze.
        height: Height of the maze.
        algorithm_name: Name of the maze generation algorithm.
        start: Starting point (S) coordinates.
        exit: Exit point (E) coordinates.

Validate Binary Tree Mazes

The Binary Tree algorithm may create mazes with no valid path between the start and exit. To validate and fix these:

    Use the process_mazes(input_dir, output_dir) function.
        input_dir: Directory with generated mazes.
        output_dir: Directory to save validated mazes.

Step 2: Test Q-Learning on a Specific Maze

   Open Q_learning.py and locate the if __name__ == "__main__": section.
   Configure the following variables:
        maze_file: Path to the maze file for testing.
        episodes (within agent.train()): Number of episodes for training.
        num_runs: Number of evaluation runs.
   Run the script to observe and print the agent's performance results for the specified maze.

Step 3: Evaluate Q-Learning on Multiple Mazes

   Open main.py and locate the if __name__ == "__main__": section.
   Use the process_all_mazes() function to evaluate all generated mazes:
        input_dir: Directory containing the generated mazes.
        csv_path: Path to the CSV file for saving results.
        runs: Number of runs per maze.
        episodes: Number of episodes per run.
   Run the script to process all mazes.
   Note: Running this script overwrites existing data in the specified CSV file. Back up your data if needed.

Step 4: Run Exploratory Data Analysis (EDA)

   Navigate to the EDA folder and open the Jupyter Notebook using an appropriate tool (e.g., Jupyter Notebook, PyCharm).
   Ensure all cells are run in the correct order for the analysis to work seamlessly.

Key Features
Machine Learning Algorithms

   Q-Learning: Tested with three configurations (Determinative, Student, Explorer).
   Optional Advanced Algorithms:
        Actor-Critic
        Deep Q-Learning (DQL)
        Deep Actor-Critic (DAC)
        Asynchronous Advantage Actor-Critic (A3C)
        AlphaZero (for complex environments)

Maze Generation

Mazes are created using:

   DFS (Depth-First Search)
   Binary Tree
   Aldous-Broder

Each algorithm represents unique real-life navigation scenarios.
Data Extraction Points

The dataset includes metrics such as:

   Number of episodes for optimal pathfinding.
   Maze size and orientation.
   Solution path length.
   Symmetry, density, and dead-end counts.
   Agent performance and success rates.

Notes and Recommendations

   Always validate mazes generated with the Binary Tree algorithm.
   Ensure directories and file paths are correctly specified.
   For detailed debugging or advanced analysis, refer to printed logs during script execution.
