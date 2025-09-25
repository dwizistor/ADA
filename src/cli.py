import argparse
import time

from src.agent import Agent
from src.algorithms.a_star import a_star
from src.algorithms.bfs import bfs
from src.algorithms.local_search import hill_climbing
from src.algorithms.ucs import ucs
from src.environment import Environment


def print_grid(grid, width, height, path, start, goal):
    for y in range(height):
        row = ""
        for x in range(width):
            if (x, y) == start:
                row += "S "
            elif (x, y) == goal:
                row += "G "
            elif (x, y) in path:
                row += "* "
            elif grid[y][x] == -1:
                row += "# "
            else:
                row += ". "
        print(row)


def load_map(map_file):
    with open(map_file, "r") as f:
        lines = f.readlines()
        width, height = map(int, lines[0].split())
        grid = []
        for i in range(1, height + 1):
            grid.append(list(map(int, lines[i].split())))

        moving_obstacles = []
        if len(lines) > height + 1:
            num_moving_obstacles = int(lines[height + 1])
            line_index = height + 2
            for _ in range(num_moving_obstacles):
                path_length = int(lines[line_index])
                line_index += 1
                path = []
                for _ in range(path_length):
                    x, y = map(int, lines[line_index].split())
                    path.append((x, y))
                    line_index += 1
                moving_obstacles.append(path)

    return grid, width, height, moving_obstacles


def main():
    parser = argparse.ArgumentParser(description="Autonomous Delivery Agent")
    parser.add_argument("--map", type=str, required=True, help="Path to the map file")
    parser.add_argument(
        "--algorithm",
        type=str,
        required=True,
        choices=["bfs", "ucs", "a_star", "local_search"],
        help="Search algorithm to use",
    )
    args = parser.parse_args()

    # Load the map
    grid, width, height, moving_obstacles = load_map(args.map)

    # Create the environment
    environment = Environment(grid, width, height)
    for obstacle_path in moving_obstacles:
        environment.add_moving_obstacle(obstacle_path)

    # Create the agent
    start = (0, 0)
    goal = (width - 1, height - 1)
    agent = Agent(environment, start, goal)

    # Find the path
    start_time = time.time()
    if args.algorithm == "bfs":
        path = agent.find_path(bfs)
    elif args.algorithm == "ucs":
        path = agent.find_path(ucs)
    elif args.algorithm == "a_star":
        path = agent.find_path(a_star)
    elif args.algorithm == "local_search":
        path = agent.find_path(hill_climbing)
    end_time = time.time()

    # Print the results
    if path:
        print(f"Path found: {path}")
        print(f"Path cost: {agent.get_path_cost()}")
        print(f"Nodes expanded: {len(path)}")
        print(f"Time taken: {end_time - start_time:.4f} seconds")
        print_grid(grid, width, height, path, start, goal)
    else:
        print("No path found.")


if __name__ == "__main__":
    main()
