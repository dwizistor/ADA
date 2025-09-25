import numpy as np

class Environment:
    """
    Represents the 2D grid environment for the autonomous delivery agent.
    """
    def __init__(self, map_path):
        """
        Initializes the environment from a map file.

        Args:
            map_path (str): The path to the map file.
        """
        self.grid = None
        self.start_pos = None
        self.goal_pos = None
        self.terrain_costs = {'.': 1, ':': 2, '*': 3, 'S': 1, 'G': 1, '#': float('inf'), 'D': float('inf')}
        self.dynamic_obstacles_initial_positions = []
        self.load_map(map_path)

    def load_map(self, map_path):
        """
        Loads the map from a text file and initializes the environment.
        """
        with open(map_path, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        self.grid = np.array([list(line) for line in lines])
        
        # Find start and goal positions
        start_pos_arr = np.where(self.grid == 'S')
        goal_pos_arr = np.where(self.grid == 'G')

        if start_pos_arr[0].size > 0:
            self.start_pos = (start_pos_arr[0][0], start_pos_arr[1][0])
        
        if goal_pos_arr[0].size > 0:
            self.goal_pos = (goal_pos_arr[0][0], goal_pos_arr[1][0])

        # Find dynamic obstacles
        dynamic_obstacle_arr = np.where(self.grid == 'D')
        for i in range(dynamic_obstacle_arr[0].size):
            pos = (dynamic_obstacle_arr[0][i], dynamic_obstacle_arr[1][i])
            self.dynamic_obstacles_initial_positions.append({'position': pos, 'direction': (0, 1)}) # Initial direction: right

    def get_cost(self, position):
        """
        Gets the movement cost for a given cell.
        """
        if not self.is_valid_position(position):
            return float('inf')
        
        char = self.grid[position[0]][position[1]]
        return self.terrain_costs.get(char, float('inf'))

    def is_valid_position(self, position):
        """
        Checks if a position is within the grid boundaries.
        """
        y, x = position
        return 0 <= y < self.grid.shape[0] and 0 <= x < self.grid.shape[1]

    def is_obstacle(self, position, time_step=0):
        """
        Checks if a position is an obstacle at a given time step.
        """
        y, x = position
        if self.grid[y][x] == '#': # Static obstacle
            return True
        
        # Check for dynamic obstacles
        for obs_data in self.dynamic_obstacles_initial_positions:
            initial_pos = obs_data['position']
            direction = obs_data['direction']
            
            # Simple oscillating movement (for now)
            # Move right for 5 steps, then left for 5 steps, etc.
            move_cycle_length = 10
            current_cycle_step = time_step % move_cycle_length
            
            current_obs_pos = initial_pos
            if current_cycle_step < move_cycle_length / 2: # Moving right
                current_obs_pos = (initial_pos[0], initial_pos[1] + current_cycle_step)
            else: # Moving left
                current_obs_pos = (initial_pos[0], initial_pos[1] + (move_cycle_length - current_cycle_step))
            
            if position == current_obs_pos:
                return True
        
        return False

    def add_obstacle(self, position):
        """
        Adds a dynamic obstacle to the grid.
        """
        self.grid[position[0]][position[1]] = '#'

    def render(self, path=None, visited=None, time_step=0):
        """
        Renders the environment to the console with custom characters.
        
        Args:
            path (list, optional): The path to draw on the grid. Defaults to None.
            visited (set, optional): The visited nodes to draw. Defaults to None.
            time_step (int): The current time step for rendering dynamic obstacles.
        """
        render_grid = np.copy(self.grid)

        # Replace characters for rendering
        render_grid[render_grid == '*'] = '.' # Treat difficult terrain as a pathway for rendering

        # Render dynamic obstacles at current time_step
        for obs_data in self.dynamic_obstacles_initial_positions:
            initial_pos = obs_data['position']
            direction = obs_data['direction']
            
            # Simple oscillating movement (for now)
            move_cycle_length = 10
            current_cycle_step = time_step % move_cycle_length
            
            current_obs_pos = initial_pos
            if current_cycle_step < move_cycle_length / 2: # Moving right
                current_obs_pos = (initial_pos[0], initial_pos[1] + current_cycle_step)
            else: # Moving left
                current_obs_pos = (initial_pos[0], initial_pos[1] + (move_cycle_length - current_cycle_step))
            
            if self.is_valid_position(current_obs_pos):
                render_grid[current_obs_pos] = 'D'


        if visited:
            for pos in visited:
                if render_grid[pos] == '.':
                    render_grid[pos] = ',' # Keep visited rendering for now

        if path:
            for pos in path:
                if render_grid[pos] not in ['S', 'G', '#', 'D']:
                    render_grid[pos] = '*'
        
        for row in render_grid:
            print(''.join(row))
