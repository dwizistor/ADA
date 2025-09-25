import heapq

def ucs(environment, start_pos, goal_pos, current_time_step=0):
    """
    Performs Uniform-Cost Search to find the cheapest path.

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

    # State in frontier, parent, cost_so_far will be (position, time_step)
    initial_state = (start_pos, current_time_step)
    frontier = [(0, initial_state)]  # (cost, (position, time_step))
    parent = {initial_state: None}
    cost_so_far = {initial_state: 0}
    
    nodes_expanded = 0

    while frontier:
        cost, current_state = heapq.heappop(frontier)
        current_pos, time_at_current_pos = current_state

        if current_pos == goal_pos:
            # Reconstruct path
            path = []
            curr = current_state
            while curr is not None:
                path.append(curr[0]) # Append only position
                curr = parent.get(curr)
            path.reverse()
            
            return path, nodes_expanded + 1, cost_so_far[current_state]

        nodes_expanded += 1

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
                    
                    # The cost of moving to a neighbor is the terrain cost of that neighbor's cell.
                    # This assumes that diagonal and cardinal moves have the same cost, which is a simplification.
                    move_cost = environment.get_cost(neighbor_pos)
                    new_cost = cost_so_far[current_state] + move_cost

                    if neighbor_state not in cost_so_far or new_cost < cost_so_far[neighbor_state]:
                        cost_so_far[neighbor_state] = new_cost
                        priority = new_cost
                        heapq.heappush(frontier, (priority, neighbor_state))
                        parent[neighbor_state] = current_state
    
    # Goal not found
    return None, nodes_expanded, 0
