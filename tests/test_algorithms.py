import unittest

from src.algorithms.a_star import a_star
from src.algorithms.bfs import bfs
from src.algorithms.local_search import hill_climbing
from src.algorithms.ucs import ucs
from src.environment import Environment


class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.environment = Environment(grid, 3, 3)
        self.start = (0, 0)
        self.goal = (2, 2)

    def test_bfs(self):
        path = bfs(self.environment, self.start, self.goal)
        self.assertIsNotNone(path)
        self.assertEqual(path[0], self.start)
        self.assertEqual(path[-1], self.goal)

    def test_ucs(self):
        path = ucs(self.environment, self.start, self.goal)
        self.assertIsNotNone(path)
        self.assertEqual(path[0], self.start)
        self.assertEqual(path[-1], self.goal)

    def test_a_star(self):
        path = a_star(self.environment, self.start, self.goal)
        self.assertIsNotNone(path)
        self.assertEqual(path[0], self.start)
        self.assertEqual(path[-1], self.goal)

    def test_hill_climbing(self):
        path = hill_climbing(self.environment, self.start, self.goal)
        self.assertIsNotNone(path)
        self.assertEqual(path[0], self.start)
        self.assertEqual(path[-1], self.goal)


if __name__ == "__main__":
    unittest.main()
