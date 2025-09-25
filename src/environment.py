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
        self.terrain_costs = {'.': 1, '*': 3, 'S': 1, 'G': 1}
        self.dynamic_obstacles = []
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

    def is_obstacle(self, position):
        """
        Checks if a position is an obstacle.
        """
        return self.grid[position[0]][position[1]] == '#'

    def add_obstacle(self, position):
        """
        Adds a dynamic obstacle to the grid.
        """
        self.grid[position[0]][position[1]] = '#'

    def render(self, path=None, visited=None):
        """
        Renders the environment to the console with a border and custom characters.
        
        Args:
            path (list, optional): The path to draw on the grid. Defaults to None.
            visited (set, optional): The visited nodes to draw. Defaults to None.
        """
        render_grid = np.copy(self.grid)

        # Replace characters for rendering
        render_grid[render_grid == '@'] = 'S'
        render_grid[render_grid == 'X'] = 'G'
        render_grid[render_grid == '*'] = '.' # Treat difficult terrain as a pathway for rendering

        if visited:
            for pos in visited:
                if render_grid[pos] == '.':
                    render_grid[pos] = ',' # Keep visited rendering for now

        if path:
            for pos in path:
                if render_grid[pos] not in ['S', 'G', '#']:
                    render_grid[pos] = '*'
        
        # Print top border
        print('-' * (self.grid.shape[1] + 2))

        for row in render_grid:
            print('|' + ''.join(row) + '|')

        # Print bottom border
        print('-' * (self.grid.shape[1] + 2))
