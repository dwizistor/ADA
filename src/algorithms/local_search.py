import random
from algorithms.a_star import a_star, heuristic

def get_path_cost(environment, path):
    """Calculates the cost of a given path."""
    cost = 0
    if not path:
        return cost
    for i in range(len(path) - 1):
        cost += environment.get_cost(path[i+1])
    return cost

def generate_random_path(environment, start_pos, goal_pos):
    """
    Generates a semi-random valid path from start to goal.
    This uses a greedy approach, always trying to move closer to the goal.
    """
    # Use A* to get an initial path and its expanded nodes
    path, nodes_expanded_a_star, _ = a_star(environment, start_pos, goal_pos)
    return path, nodes_expanded_a_star

def get_neighbor(environment, path, original_start, original_goal):
    """
    Gets a neighboring path by modifying a sub-path.
    original_start and original_goal are needed for the a_star call.
    """
    if len(path) < 4:
        return path

    p1_index = random.randint(1, len(path) - 3)
    p2_index = random.randint(p1_index + 1, len(path) - 2)

    sub_path, nodes_expanded_a_star, _ = a_star(environment, path[p1_index - 1], path[p2_index + 1])

    if sub_path:
        return path[:p1_index] + sub_path[1:-1] + path[p2_index:], nodes_expanded_a_star
    else:
        return path, nodes_expanded_a_star # Return original path and its expanded nodes if no sub-path is found

def hill_climbing_replan(environment, start_pos, goal_pos, current_time_step=0):
    """
    Replanning using hill-climbing with random restarts.
    """
    num_restarts = 20
    max_iterations = 50 # To prevent getting stuck
    best_path = None
    best_cost = float('inf')
    total_nodes_expanded = 0

    for _ in range(num_restarts):
        # Generate a random initial path
        current_path, nodes_expanded_initial = generate_random_path(environment, start_pos, goal_pos)
        total_nodes_expanded += nodes_expanded_initial

        if not current_path:
            continue
            
        current_cost = get_path_cost(environment, current_path)

        for _ in range(max_iterations):
            neighbor_path, nodes_expanded_neighbor = get_neighbor(environment, current_path, start_pos, goal_pos)
            total_nodes_expanded += nodes_expanded_neighbor

            neighbor_cost = get_path_cost(environment, neighbor_path)

            if neighbor_cost < current_cost:
                current_path = neighbor_path
                current_cost = neighbor_cost
            else:
                break
        
        if current_cost < best_cost:
            best_path = current_path
            best_cost = current_cost
            
    return best_path, total_nodes_expanded, best_cost