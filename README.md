# Autonomous Delivery Agent

This project is an implementation of an autonomous delivery agent that navigates a 2D grid city.

## Description

The agent is designed to deliver packages efficiently by navigating a grid-based environment with various challenges:
- Static obstacles
- Varying terrain costs
- Dynamic moving obstacles

The agent uses different search algorithms to find the optimal path and can re-plan its route in response to dynamic changes in the environment.

## Features

- **Pathfinding Algorithms:**
  - Uninformed Search: Breadth-First Search (BFS), Uniform-Cost Search (UCS)
  - Informed Search: A* Search
  - Local Search: Hill-Climbing with random restarts for replanning
- **Dynamic Replanning:** The agent can adapt to moving obstacles by replanning its path.
- **CLI Interface:** A command-line interface to run simulations with different maps and algorithms.
- **Visual Output:** The agent's navigation is visualized in the terminal.

## Getting Started

### Prerequisites

- Python 3.x
- Dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd autonomous-delivery-agent
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

To run a simulation, use the `cli.py` script. For example:

```bash
python src/cli.py maps/small.txt --algorithm a_star
```

## Map Format

The maps are represented as text files with the following characters:

- `@`: Agent's starting position
- `X`: Package delivery destination
- `#`: Static obstacle (wall)
- `.`: Normal terrain (movement cost of 1)
- `*`: Difficult terrain (e.g., sand, mud) with a higher movement cost.
- `D`: Dynamic obstacle (e.g., another vehicle)

## Experimental Results and Analysis

We compared the performance of Breadth-First Search (BFS), A* Search, and Local Search (Hill-Climbing with Random Restarts) on various grid maps. The metrics used for comparison were: Path Cost, Nodes Expanded, and Time Taken (in milliseconds).

### Small Map (`maps/small.txt`)

| Algorithm    | Path Found | Cost | Nodes Expanded | Time (ms) |
| :----------- | :--------- | :--- | :------------- | :-------- |
| BFS          | Yes        | 7.00 | 18             | 0.2716    |
| A_STAR       | Yes        | 5.00 | 9              | 0.2079    |
| LOCAL_SEARCH | Yes        | 6.00 | 0              | 5.8410    |

**Analysis:**
On the small map, all algorithms successfully found a path.
- **BFS** found a path with 7.00 cost, expanding 18 nodes. As an uninformed search, it prioritizes the shortest path in terms of steps, which in this case led through a costly terrain cell.
- **A* Search** found an optimal path with a lower cost of 5.00, expanding only 9 nodes. This highlights the effectiveness of A*'s admissible heuristic in guiding the search towards the goal, leading to fewer explored states.
- **Local Search (Hill-Climbing)** also found a path with a cost of 6.00. It is important to note that local search algorithms do not guarantee optimality and may get stuck in local minima. The 'Nodes Expanded' metric is not directly applicable to local search in the same way as for graph search algorithms.

### Medium Map (`maps/medium.txt`)

| Algorithm    | Path Found | Cost | Nodes Expanded | Time (ms) |
| :----------- | :--------- | :--- | :------------- | :-------- |
| BFS          | Yes        | 7.00 | 18             | 0.2572    |
| A_STAR       | Yes        | 5.00 | 9              | 0.2008    |
| LOCAL_SEARCH | Yes        | 6.00 | 0              | 7.1970    |

**Analysis:**
The results on the medium map are consistent with the small map.
- **BFS** found a path with 7.00 cost, prioritizing fewer steps.
- **A* Search** again found the optimal path with the fewest nodes expanded (9), showcasing its superior efficiency due to heuristic guidance.
- **Local Search (Hill-Climbing)** found a path with a cost of 6.00. Its performance is highly dependent on the initial random path and the neighbor generation strategy.

### Large Map (`maps/large.txt`)

| Algorithm    | Path Found | Cost | Nodes Expanded | Time (ms) |
| :----------- | :--------- | :--- | :------------- | :-------- |
| BFS          | No         | -    | 25             | 0.3235    |
| A_STAR       | No         | -    | 26             | 0.4830    |
| LOCAL_SEARCH | No         | -    | 0              | 5.1126    |

**Analysis:**
On the complex large map, none of the implemented algorithms were able to find a path. The low number of nodes expanded for BFS and A* (25-26) suggests that the search quickly exhausted its options or encountered an unsolvable section of the maze. This indicates that the provided `large.txt` map might be inherently unsolvable for these algorithms within a reasonable search depth, or it contains a very intricate path that requires more extensive exploration than these algorithms performed in this setup. Local Search also failed to find a path, which is expected if no valid initial path can be generated or if it gets stuck in a local minimum.

### Dynamic Map (`maps/dynamic.txt`)

| Algorithm    | Path Found | Cost  | Nodes Expanded | Time (ms) |
| :----------- | :--------- | :---- | :------------- | :-------- |
| BFS          | Yes        | 11.00 | 48             | 0.7642    |
| A_STAR       | Yes        | 11.00 | 36             | 1.2804    |
| LOCAL_SEARCH | Yes        | 11.00 | 0              | 18.1782   |

**Analysis:**
On the dynamic map, all algorithms successfully found an initial path. The costs and nodes expanded are consistent with their respective search strategies. Local Search, while finding an optimal path in this simple scenario, took significantly longer due to its iterative nature and random restarts.

### General Conclusions

- **BFS** is suitable for finding the shortest path in terms of steps, but it does not consider varying terrain costs, potentially leading to more expensive paths.
- **A* Search** is generally the most efficient algorithm for finding optimal (cheapest) paths, especially in environments with varying costs, due to its use of an admissible heuristic to guide the search.
- **Local Search (Hill-Climbing)** can be effective for replanning in dynamic environments, but it does not guarantee optimality and its performance is highly dependent on the quality of initial paths and neighbor generation. The 'Nodes Expanded' metric is not directly comparable to graph search algorithms.
- For highly complex or potentially unsolvable mazes, these basic search algorithms may struggle to find a path or exhaust their search space quickly. More advanced techniques or a different maze design might be necessary for such scenarios.
