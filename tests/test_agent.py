import unittest

from src.agent import Agent
from src.algorithms.bfs import bfs
from src.environment import Environment


class TestAgent(unittest.TestCase):
    def setUp(self):
        grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        environment = Environment(grid, 3, 3)
        self.agent = Agent(environment, (0, 0), (2, 2))

    def test_find_path(self):
        path = self.agent.find_path(bfs)
        self.assertIsNotNone(path)
        self.assertEqual(path[0], (0, 0))
        self.assertEqual(path[-1], (2, 2))

    def test_get_path_cost(self):
        self.agent.path = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
        self.assertEqual(self.agent.get_path_cost(), 5)


if __name__ == "__main__":
    unittest.main()
