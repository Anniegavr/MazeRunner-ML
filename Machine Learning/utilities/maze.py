
class Maze:
    def __init__(self, grid, start, exit):
        self.grid = grid
        self.start = start  
        self.exit = exit    

    def valid_move(self, current, action):
      #Returns the next state based on action (0: Up, 1: Right, 2: Down, 3: Left)
      x, y = current
      movements = [(-1, 0), (0, 1), (1, 0), (0, -1)]
      dx, dy = movements[action]
      new_x, new_y = x + dx, y + dy

      # Check if the new position is within bounds and not a wall
      if 0 <= new_x < len(self.grid[0]) and 0 <= new_y < len(self.grid):
            if self.grid[new_y][new_x] == 0:  # Walkable space
                return (new_x, new_y)
      
      return current # Return current position if move is invalid

    def step(self, state, action):
        """
        Takes the agent's action and moves the agent accordingly.
        Returns the next state, reward, and whether the episode is done.
        """
        next_state = self.valid_move(state, action)
        distance_to_exit = abs(next_state[0] - self.exit[0]) + abs(next_state[1] - self.exit[1])
        current_distance = abs(state[0] - self.exit[0]) + abs(state[1] - self.exit[1])
        
        # Define rewards
        reward = -1 # Defaul penalty for each step
        done = False
        
        if next_state == self.exit:
            reward = 100
            done = True
        elif distance_to_exit < current_distance:
            reward += 0.2 # Small reward for moving closer
        
        return next_state, reward, done
        

  
