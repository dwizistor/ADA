from algorithms.bfs import bfs
from algorithms.ucs import ucs
from algorithms.a_star import a_star
from algorithms.local_search import hill_climbing_replan

class Agent:
    """
    The autonomous delivery agent.
    """
    def __init__(self, environment):
        """
        Initializes the agent.

        Args:
            environment (Environment): The environment the agent operates in.
        """
        self.environment = environment
        self.algorithm = None

    def set_algorithm(self, algorithm_name):
        """
        Sets the pathfinding algorithm to use.

        Args:
            algorithm_name (str): The name of the algorithm ('bfs', 'ucs', 'a_star', 'local_search').
        """
        if algorithm_name == 'bfs':
            self.algorithm = bfs
        elif algorithm_name == 'ucs':
            self.algorithm = ucs
        elif algorithm_name == 'a_star':
            self.algorithm = a_star
        elif algorithm_name == 'local_search':
            self.algorithm = hill_climbing_replan
        else:
            raise ValueError(f"Unknown algorithm: {algorithm_name}")

    def find_path(self):
        """
        Finds a path from start to goal using the selected algorithm.

        Returns:
            The result from the pathfinding algorithm, which is typically
            (path, nodes_expanded, cost).
        """
        if not self.algorithm:
            raise Exception("Algorithm not set. Call set_algorithm() first.")
        
        return self.algorithm(self.environment, self.environment.start_pos, self.environment.goal_pos)
