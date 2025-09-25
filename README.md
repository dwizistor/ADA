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
   git clone https://github.com/dwizistor/ada.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ada
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

- `S`: Agent's starting position
- `G`: Package delivery destination
- `#`: Static obstacle (wall)
- `.`: Normal terrain (movement cost of 1)
- `:`: Difficult terrain (movement cost of 2)
- `*`: Solution terrain
- `D`: Dynamic obstacle (e.g., another vehicle)

## Experimental Results and Analysis

We compared the performance of Breadth-First Search (BFS), A* Search, and Local Search (Hill-Climbing with Random Restarts) on various grid maps. The metrics used for comparison were: Path Cost, Nodes Expanded, and Time Taken (in milliseconds).

### Small Map (`maps/small.txt`)

| Algorithm    | Path Found | Cost | Nodes Expanded | Time (ms) |
| :----------- | :--------- | :--- | :------------- | :-------- |
| BFS          | Yes        | 6.00 | 58             | 1.0093    |
| A_STAR       | Yes        | 5.00 | 9              | 0.2959    |
| LOCAL_SEARCH | Yes        | 5.00 | 298            | 7.4840    |

**Analysis:**
On the small map, all algorithms successfully found a path.
- **BFS** found a path with 6.00 cost, expanding 58 nodes. As an uninformed search, it prioritizes the shortest path in terms of steps, which in this case led through a costly terrain cell.
- **A* Search** found an optimal path with a lower cost of 5.00, expanding only 9 nodes. This highlights the effectiveness of A*'s admissible heuristic in guiding the search towards the goal, leading to fewer explored states.
- **Local Search (Hill-Climbing)** also found a path with a cost of 5.00. It is important to note that local search algorithms do not guarantee optimality and may get stuck in local minima. The 'Nodes Expanded' metric for local search represents the total nodes expanded by the internal A* calls during path generation and neighbor exploration.

### Medium Map (`maps/medium.txt`)

| Algorithm    | Path Found | Cost | Nodes Expanded | Time (ms) |
| :----------- | :--------- | :--- | :------------- | :-------- |
| BFS          | Yes        | 6.00 | 58             | 0.8478    |
| A_STAR       | Yes        | 5.00 | 9              | 0.2294    |
| LOCAL_SEARCH | Yes        | 5.00 | 301            | 6.6995    |

**Analysis:**
The results on the medium map are consistent with the small map.
- **BFS** found a path with 6.00 cost, prioritizing fewer steps.
- **A* Search** again found the optimal path with the fewest nodes expanded (9), showcasing its superior efficiency due to heuristic guidance.
- **Local Search (Hill-Climbing)** found a path with a cost of 5.00. Its performance is highly dependent on the initial random path and the neighbor generation strategy. The 'Nodes Expanded' metric for local search represents the total nodes expanded by the internal A* calls during path generation and neighbor exploration.

### Large Map (`maps/large.txt`)

| Algorithm    | Path Found | Cost  | Nodes Expanded | Time (ms) |
| :----------- | :--------- | :---- | :------------- | :-------- |
| BFS          | Yes        | 32.00 | 2185           | 25.2394   |
| A_STAR       | Yes        | 32.00 | 271            | 4.5824    |
| LOCAL_SEARCH | Yes        | 32.00 | 6744           | 116.7434  |

**Analysis:**
On the complex large map, all implemented algorithms were able to find a path. BFS and A* found the optimal path with a cost of 32.00. A* was more efficient, expanding fewer nodes. Local Search found a path with a cost of 32.00, which is optimal in this case. The 'Nodes Expanded' metric for local search represents the total nodes expanded by the internal A* calls during path generation and neighbor exploration.

### Dynamic Map (`maps/dynamic.txt`)

| Algorithm    | Path Found | Cost  | Nodes Expanded | Time (ms) |
| :----------- | :--------- | :---- | :------------- | :-------- |
| BFS          | Yes        | 11.00 | 296            | 4.7485    |
| A_STAR       | Yes        | 11.00 | 34             | 1.0788    |
| LOCAL_SEARCH | Yes        | 11.00 | 888            | 26.1861   |

**Analysis:**
On the dynamic map, all algorithms successfully found an initial path. The costs and nodes expanded are consistent with their respective search strategies. Local Search, while finding an optimal path in this simple scenario, took significantly longer due to its iterative nature and random restarts. The 'Nodes Expanded' metric for local search represents the total nodes expanded by the internal A* calls during path generation and neighbor exploration.

### General Conclusions

- **BFS** is suitable for finding the shortest path in terms of steps, but it does not consider varying terrain costs, potentially leading to more expensive paths.
- **A* Search** is generally the most efficient algorithm for finding optimal (cheapest) paths, especially in environments with varying costs, due to its use of an admissible heuristic to guide the search.
- **Local Search (Hill-Climbing)** can be effective for replanning in dynamic environments, but it does not guarantee optimality and its performance is highly dependent on the quality of initial paths and neighbor generation. The 'Nodes Expanded' metric for local search represents the total nodes expanded by the internal A* calls during path generation and neighbor exploration.
- For highly complex mazes, A* and BFS can find optimal paths, but Local Search may find suboptimal paths or fail to find a path if it gets stuck in a local minimum. The efficiency of A* makes it a strong choice for such scenarios.
