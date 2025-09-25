import heapq


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def a_star(environment, start, goal):
    priority_queue = [(0, start, [start])]
    visited = {start}

    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path

        for neighbor in environment.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                new_cost = cost + environment.get_cost(neighbor)
                priority = new_cost + manhattan_distance(neighbor, goal)
                heapq.heappush(priority_queue, (priority, neighbor, path + [neighbor]))

    return None
