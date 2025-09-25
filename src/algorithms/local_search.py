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
    path = [start_pos]
    current_pos = start_pos
    
    # Limit path length to avoid infinite loops
    for _ in range(environment.grid.size):
        if current_pos == goal_pos:
            break

        neighbors = []
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue
                
                neighbor_pos = (current_pos[0] + dy, current_pos[1] + dx)
                
                if (environment.is_valid_position(neighbor_pos) and
                        not environment.is_obstacle(neighbor_pos) and
                        neighbor_pos not in path):
                    neighbors.append(neighbor_pos)
        
        if not neighbors:
            return None # Stuck

        neighbors.sort(key=lambda pos: heuristic(pos, goal_pos))
        
        best_heuristic = heuristic(neighbors[0], goal_pos)
        best_neighbors = [n for n in neighbors if heuristic(n, goal_pos) == best_heuristic]
        
        next_pos = random.choice(best_neighbors)
        path.append(next_pos)
        current_pos = next_pos
        
    return path if current_pos == goal_pos else None

def get_neighbor(environment, path):
    """Gets a neighboring path by modifying a sub-path."""
    if len(path) < 4:
        return path

    p1_index = random.randint(1, len(path) - 3)
    p2_index = random.randint(p1_index + 1, len(path) - 2)

    original_start = environment.start_pos
    original_goal = environment.goal_pos

    environment.start_pos = path[p1_index - 1]
    environment.goal_pos = path[p2_index + 1]

    sub_path, _, _ = a_star(environment)

    # Restore original start and goal
    environment.start_pos = original_start
    environment.goal_pos = original_goal

    if sub_path:
        return path[:p1_index] + sub_path[1:-1] + path[p2_index:]
    else:
        return path

def hill_climbing_replan(environment):
    """
    Replanning using hill-climbing with random restarts.
    """
    num_restarts = 20
    max_iterations = 50 # To prevent getting stuck
    best_path = None
    best_cost = float('inf')

    for _ in range(num_restarts):
        current_path = generate_random_path(environment, environment.start_pos, environment.goal_pos)
        if not current_path:
            continue
            
        current_cost = get_path_cost(environment, current_path)

        for _ in range(max_iterations):
            neighbor_path = get_neighbor(environment, current_path)
            neighbor_cost = get_path_cost(environment, neighbor_path)

            if neighbor_cost < current_cost:
                current_path = neighbor_path
                current_cost = neighbor_cost
            else:
                break
        
        if current_cost < best_cost:
            best_path = current_path
            best_cost = current_cost
            
    return best_path, 0, best_cost