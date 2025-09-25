# Project Requirements

## Functional Requirements

*   **Environment Modeling:**
    *   The environment must be modeled as a 2D grid.
    *   The grid must support static obstacles (e.g., walls, buildings).
    *   The grid must support varying terrain costs (e.g., roads, grass, water).
    *   The grid must support dynamic moving obstacles (e.g., other vehicles).
*   **Agent:**
    *   The agent must be able to navigate the 2D grid city.
    *   The agent must be able to deliver packages to specified locations.
    *   The agent must be rational, choosing actions that maximize delivery efficiency under constraints (time, fuel).
*   **Pathfinding Algorithms:**
    *   Implement an uninformed search algorithm (BFS or Uniform-cost).
    *   Implement an informed search algorithm (A* with an admissible heuristic).
    *   Implement a local search replanning strategy (e.g., hill-climbing with random restarts or simulated annealing) to handle dynamic obstacles.
*   **Experimental Comparison:**
    *   Compare the implemented algorithms experimentally on several map instances.
    *   Report the results, including path cost, nodes expanded, and time taken.
*   **Analysis:**
    *   Provide an analysis describing when each method performs better and why.

## Non-Functional Requirements

*   **Source Code:**
    *   The source code must be well-documented.
    *   The project should be implemented in Python (or another language of your choice).
    *   A command-line interface (CLI) must be provided to run each planner.
    *   The code should be committed to a Git repository.
    *   The project must include tests to ensure reproducibility.
*   **Proof-of-Concept:**
    *   At least one proof-of-concept of dynamic replanning must be provided (e.g., a log showing an obstacle appearing and the agent replanning).
*   **Test Maps:**
    *   At least four test maps must be provided:
        *   Small
        *   Medium
        *   Large
        *   One with dynamic obstacles (moving vehicles).
    *   The grid file format must be included.
*   **Report:**
    *   A short report (maximum 6 pages) must be submitted, containing:
        *   Environment model
        *   Agent design
        *   Heuristics used
        *   Experimental results (tables + short plots)
        *   Analysis and conclusion
*   **Demo:**
    *   A short recorded demo (5 minutes) or a sequence of screenshots showing the agent acting on a dynamic map must be submitted.

## Constraints and Assumptions

*   Grid cells have an integer movement cost of at least 1 (representing different terrains).
*   Moving obstacles occupy cells and move deterministically according to a known schedule (so the agent can plan knowing future positions for one horizon) or unpredictably (for local search testing).
*   The agent can move in four directions (up, down, left, right). Diagonal movement is optional and should be stated in the report.
