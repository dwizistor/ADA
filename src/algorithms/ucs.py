import heapq


def ucs(environment, start, goal):
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
                heapq.heappush(priority_queue, (new_cost, neighbor, path + [neighbor]))

    return None
