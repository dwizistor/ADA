import unittest

from src.environment import Environment


class TestEnvironment(unittest.TestCase):
    def setUp(self):
        grid = [[1, 1, 1], [1, -1, 1], [1, 1, 1]]
        self.environment = Environment(grid, 3, 3)

    def test_get_cost(self):
        self.assertEqual(self.environment.get_cost((0, 0)), 1)
        self.assertEqual(self.environment.get_cost((1, 1)), -1)

    def test_is_valid(self):
        self.assertTrue(self.environment.is_valid((0, 0)))
        self.assertFalse(self.environment.is_valid((3, 3)))

    def test_is_obstacle(self):
        self.assertTrue(self.environment.is_obstacle((1, 1)))
        self.assertFalse(self.environment.is_obstacle((0, 0)))

    def test_get_neighbors(self):
        neighbors = self.environment.get_neighbors((0, 0))
        self.assertEqual(len(neighbors), 2)
        self.assertIn((0, 1), neighbors)
        self.assertIn((1, 0), neighbors)


if __name__ == "__main__":
    unittest.main()
