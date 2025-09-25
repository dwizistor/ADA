from collections import deque

def bfs(environment, start_pos, goal_pos, current_time_step=0):
    """
    Performs Breadth-First Search to find the shortest path in terms of number of steps.

    Args:
        environment (Environment): The environment to search in.
        start_pos (tuple): The starting position (y, x).
        goal_pos (tuple): The goal position (y, x).
        current_time_step (int): The current time step of the agent.

    Returns:
        tuple: A tuple containing:
            - list: The path from start to goal as a list of coordinates.
            - int: The number of nodes expanded.
            - float: The cost of the path (for BFS, this is the length of the path).
    """

    # State in frontier, visited, parent will be (position, time_step)
    initial_state = (start_pos, current_time_step)
    frontier = deque([initial_state])
    visited = {initial_state}
    parent = {initial_state: None}
    
    nodes_expanded = 0

    while frontier:
        current_state = frontier.popleft()
        current_pos, time_at_current_pos = current_state
        nodes_expanded += 1

        if current_pos == goal_pos:
            # Reconstruct path
            path = []
            cost = 0
            curr = current_state
            while curr is not None:
                path.append(curr[0]) # Append only position
                if parent.get(curr) is not None:
                    cost += environment.get_cost(curr[0])
                curr = parent.get(curr)
            path.reverse()

            return path, nodes_expanded, cost

        # 8-connected movement
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue

                neighbor_pos = (current_pos[0] + dy, current_pos[1] + dx)
                time_at_neighbor_pos = time_at_current_pos + 1
                neighbor_state = (neighbor_pos, time_at_neighbor_pos)

                if (environment.is_valid_position(neighbor_pos) and
                        not environment.is_obstacle(neighbor_pos, time_at_neighbor_pos) and
                        neighbor_state not in visited):
                    
                    visited.add(neighbor_state)
                    parent[neighbor_state] = current_state
                    frontier.append(neighbor_state)
    
    # Goal not found
    return None, nodes_expanded, 0
