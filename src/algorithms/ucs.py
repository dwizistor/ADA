import heapq

def ucs(environment):
    """
    Performs Uniform-Cost Search to find the cheapest path.

    Args:
        environment (Environment): The environment to search in.

    Returns:
        tuple: A tuple containing:
            - list: The path from start to goal as a list of coordinates.
            - int: The number of nodes expanded.
            - float: The cost of the path.
    """
    start_pos = environment.start_pos
    goal_pos = environment.goal_pos

    frontier = [(0, start_pos)]  # (cost, position)
    parent = {start_pos: None}
    cost_so_far = {start_pos: 0}
    
    nodes_expanded = 0

    while frontier:
        cost, current_pos = heapq.heappop(frontier)

        if current_pos == goal_pos:
            # Reconstruct path
            path = []
            curr = goal_pos
            while curr is not None:
                path.append(curr)
                curr = parent.get(curr)
            path.reverse()
            
            return path, nodes_expanded + 1, cost_so_far[goal_pos]

        nodes_expanded += 1

        # 8-connected movement
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue

                neighbor_pos = (current_pos[0] + dy, current_pos[1] + dx)

                if (environment.is_valid_position(neighbor_pos) and
                        not environment.is_obstacle(neighbor_pos)):
                    
                    # The cost of moving to a neighbor is the terrain cost of that neighbor's cell.
                    # This assumes that diagonal and cardinal moves have the same cost, which is a simplification.
                    move_cost = environment.get_cost(neighbor_pos)
                    new_cost = cost_so_far[current_pos] + move_cost

                    if neighbor_pos not in cost_so_far or new_cost < cost_so_far[neighbor_pos]:
                        cost_so_far[neighbor_pos] = new_cost
                        priority = new_cost
                        heapq.heappush(frontier, (priority, neighbor_pos))
                        parent[neighbor_pos] = current_pos
    
    # Goal not found
    return None, nodes_expanded, 0
