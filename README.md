# Autonomous Delivery Agent

This project implements an autonomous delivery agent that navigates a 2D grid city to deliver packages efficiently. The agent is designed to be rational, choosing actions that maximize delivery efficiency while considering constraints like time and fuel.

## Features

*   **Environment Modeling:** The agent can model the environment, including static obstacles, varying terrain costs, and dynamic moving obstacles.
*   **Pathfinding Algorithms:** The project implements and compares the following search algorithms:
    *   Uninformed Search: Breadth-First Search (BFS) and Uniform-Cost Search (UCS).
    *   Informed Search: A* with an admissible heuristic.
    *   Local Search: A replanning strategy (e.g., hill-climbing with random restarts or simulated annealing) to handle dynamic obstacles and changing traffic costs.
*   **Experimental Comparison:** The algorithms are compared experimentally on several map instances, with results reported for path cost, nodes expanded, and time taken.
*   **Analysis:** The project provides an analysis of when each method performs better and why.

## Project Structure

```
/
|-- README.md
|-- requirements.md
|-- src/
|   |-- agent.py
|   |-- environment.py
|   |-- algorithms/
|   |   |-- __init__.py
|   |   |-- bfs.py
|   |   |-- ucs.py
|   |   |-- a_star.py
|   |   |-- local_search.py
|   |-- cli.py
|-- maps/
|   |-- small.txt
|   |-- medium.txt
|   |-- large.txt
|   |-- dynamic.txt
|-- report/
|   |-- report.md
|-- tests/
|   |-- test_agent.py
|   |-- test_environment.py
|   |-- test_algorithms.py
```

## Getting Started

### Prerequisites

*   Python 3.x
*   Additional dependencies can be found in `requirements.txt`.

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/autonomous-delivery-agent.git
    ```
2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

The project provides a command-line interface (CLI) to run each planner.

To run a specific algorithm on a map, use the following command:

```bash
python src/cli.py --map maps/small.txt --algorithm bfs
```

### Options

*   `--map`: Path to the map file.
*   `--algorithm`: The search algorithm to use (`bfs`, `ucs`, `a_star`, `local_search`).

## Map File Format

A map file is a plain text file with the following structure:

1.  **First Line**: Two integers representing the `width` and `height` of the grid, separated by a space.
    *   Example: `5 5` (for a 5x5 grid)

2.  **Grid Definition**: `height` number of lines follow, each containing `width` number of integers separated by spaces. These integers represent the cost of traversing that cell. A value of `-1` typically denotes an obstacle.
    *   Example (for a 5x5 grid):
        ```
        1 1 1 1 1
        1 -1 1 -1 1
        1 1 1 1 1
        1 -1 1 -1 1
        1 1 1 1 1
        ```

3.  **Moving Obstacles (Optional)**: If there are moving obstacles, they are defined after the grid.
    *   **Line 1**: A single integer indicating the `number of moving obstacles`.
    *   For each moving obstacle:
        *   **Line 1**: A single integer indicating the `path length` for this obstacle.
        *   **Following `path_length` lines**: Each line contains two integers `x y` representing the (x, y) coordinates of the obstacle at each time step.

**Example of a complete map file:**

```
5 5
1 1 1 1 1
1 -1 1 -1 1
1 1 1 1 1
1 -1 1 -1 1
1 1 1 1 1
1
3
0 1
1 1
2 1
```

## Running Tests

To run the tests, use the following command:

```bash
pytest
```

## Report

The project report can be found in the `report` directory. It contains a detailed analysis of the environment model, agent design, heuristics used, experimental results, and a conclusion.

## Demo

A short recorded demo or a sequence of screenshots showing the agent acting on a dynamic map is available in the `demo` directory.
