import random


def generate_map(width, height, num_obstacles, moving_obstacle_length):
    # Create an empty grid
    grid = [[1 for _ in range(width)] for _ in range(height)]

    # Add random obstacles
    for _ in range(num_obstacles):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        grid[y][x] = -1

    # Create a moving obstacle path
    moving_obstacle = []
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    for _ in range(moving_obstacle_length):
        moving_obstacle.append((x, y))
        # Move the obstacle randomly
        dx = random.randint(-1, 1)
        dy = random.randint(-1, 1)
        x = max(0, min(width - 1, x + dx))
        y = max(0, min(height - 1, y + dy))

    return grid, [moving_obstacle]


def save_map(file_path, grid, moving_obstacles):
    with open(file_path, "w") as f:
        # Write dimensions
        f.write(f"{len(grid[0])} {len(grid)}\n")

        # Write grid
        for row in grid:
            f.write(" ".join(map(str, row)) + "\n")

        # Write moving obstacles
        f.write(f"{len(moving_obstacles)}\n")
        for path in moving_obstacles:
            f.write(f"{len(path)}\n")
            for x, y in path:
                f.write(f"{x} {y}\n")


if __name__ == "__main__":
    grid, moving_obstacles = generate_map(50, 50, 200, 50)
    save_map("maps/finalmap.txt", grid, moving_obstacles)
