class Agent:
    def __init__(self, environment, start, goal):
        self.environment = environment
        self.start = start
        self.goal = goal
        self.path = []

    def find_path(self, algorithm):
        self.path = algorithm(self.environment, self.start, self.goal)
        return self.path

    def get_path_cost(self):
        cost = 0
        for position in self.path:
            cost += self.environment.get_cost(position)
        return cost
