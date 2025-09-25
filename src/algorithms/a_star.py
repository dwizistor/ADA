import heapq

def heuristic(a, b):
    """
    Calculates the Chebyshev distance between two points.
    This is an admissible heuristic for an 8-connected grid.
    """
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

def a_star(environment, start_pos, goal_pos, current_time_step=0):
    """
    Performs A* search to find the cheapest path.

    Args:
        environment (Environment): The environment to search in.
        start_pos (tuple): The starting position (y, x).
        goal_pos (tuple): The goal position (y, x).
        current_time_step (int): The current time step of the agent.

    Returns:
        tuple: A tuple containing:
            - list: The path from start to goal as a list of coordinates.
            - int: The number of nodes expanded.
            - float: The cost of the path.
    """

    # State in frontier, parent, g_cost will be (position, time_step)
    initial_state = (start_pos, current_time_step)
    frontier = [(0, initial_state)]  # (f_cost, (position, time_step))
    parent = {initial_state: None}
    g_cost = {initial_state: 0}
    
    nodes_expanded = 0

    while frontier:
        _, current_state = heapq.heappop(frontier)
        current_pos, time_at_current_pos = current_state
        nodes_expanded += 1

        if current_pos == goal_pos:
            # Reconstruct path
            path = []
            curr = current_state
            while curr is not None:
                path.append(curr[0]) # Append only position
                curr = parent.get(curr)
            path.reverse()
            
            return path, nodes_expanded, g_cost[current_state]

        # 8-connected movement
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue

                neighbor_pos = (current_pos[0] + dy, current_pos[1] + dx)
                time_at_neighbor_pos = time_at_current_pos + 1
                neighbor_state = (neighbor_pos, time_at_neighbor_pos)

                if (environment.is_valid_position(neighbor_pos) and
                        not environment.is_obstacle(neighbor_pos, time_at_neighbor_pos)):
                    
                    move_cost = environment.get_cost(neighbor_pos)
                    new_g_cost = g_cost[current_state] + move_cost

                    if neighbor_state not in g_cost or new_g_cost < g_cost[neighbor_state]:
                        g_cost[neighbor_state] = new_g_cost
                        h_cost = heuristic(neighbor_pos, goal_pos)
                        f_cost = new_g_cost + h_cost
                        heapq.heappush(frontier, (f_cost, neighbor_state))
                        parent[neighbor_state] = current_state
    
    # Goal not found
    return None, nodes_expanded, 0
