

class Environment:
    def __init__(self, grid, width, height):
        self.grid = grid
        self.width = width
        self.height = height
        self.moving_obstacles = []

    def get_cost(self, position):
        x, y = position
        return self.grid[y][x]

    def is_valid(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def is_obstacle(self, position):
        x, y = position
        return self.grid[y][x] == -1

    def get_neighbors(self, position):
        x, y = position
        neighbors = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if self.is_valid((new_x, new_y)) and not self.is_obstacle((new_x, new_y)):
                neighbors.append((new_x, new_y))
        return neighbors

    def add_moving_obstacle(self, obstacle_path):
        self.moving_obstacles.append(obstacle_path)

    def is_obstacle_at_time(self, position, time):
        if self.is_obstacle(position):
            return True
        for obstacle_path in self.moving_obstacles:
            if time < len(obstacle_path) and obstacle_path[time] == position:
                return True
        return False
