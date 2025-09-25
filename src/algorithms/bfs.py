from collections import deque

def bfs(environment):
    """
    Performs Breadth-First Search to find the shortest path in terms of number of steps.

    Args:
        environment (Environment): The environment to search in.

    Returns:
        tuple: A tuple containing:
            - list: The path from start to goal as a list of coordinates.
            - int: The number of nodes expanded.
            - float: The cost of the path (for BFS, this is the length of the path).
    """
    start_pos = environment.start_pos
    goal_pos = environment.goal_pos

    frontier = deque([start_pos])
    visited = {start_pos}
    parent = {start_pos: None}
    
    nodes_expanded = 0

    while frontier:
        current_pos = frontier.popleft()
        nodes_expanded += 1

        if current_pos == goal_pos:
            # Reconstruct path
            path = []
            cost = 0
            curr = goal_pos
            while curr is not None:
                path.append(curr)
                if parent.get(curr) is not None:
                    cost += environment.get_cost(curr)
                curr = parent.get(curr)
            path.reverse()

            return path, nodes_expanded, cost

        # 8-connected movement
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue

                neighbor_pos = (current_pos[0] + dy, current_pos[1] + dx)

                if (environment.is_valid_position(neighbor_pos) and
                        not environment.is_obstacle(neighbor_pos) and
                        neighbor_pos not in visited):
                    
                    visited.add(neighbor_pos)
                    parent[neighbor_pos] = current_pos
                    frontier.append(neighbor_pos)
    
    # Goal not found
    return None, nodes_expanded, 0
