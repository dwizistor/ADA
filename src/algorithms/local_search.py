

def hill_climbing(environment, start, goal, max_restarts=10):
    for _ in range(max_restarts):
        path, cost = random_restart_hill_climbing(environment, start, goal)
        if path:
            return path
    return None


def random_restart_hill_climbing(environment, start, goal):
    current = start
    path = [current]
    cost = 0

    while current != goal:
        neighbors = environment.get_neighbors(current)
        if not neighbors:
            return None, float("inf")

        best_neighbor = min(neighbors, key=lambda n: manhattan_distance(n, goal))
        path.append(best_neighbor)
        cost += environment.get_cost(best_neighbor)
        current = best_neighbor

    return path, cost


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
