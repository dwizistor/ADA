import argparse
from environment import Environment
from agent import Agent

import time

def main():
    """
    Main function to run the autonomous delivery agent simulation.
    """
    parser = argparse.ArgumentParser(description="Autonomous Delivery Agent")
    parser.add_argument("map_file", help="Path to the map file.")
    parser.add_argument("--algorithm", choices=['bfs', 'ucs', 'a_star', 'local_search'], 
                        default='a_star', help="Search algorithm to use.")
    parser.add_argument("--dynamic", action='store_true', help="Demonstrate dynamic replanning.")
    parser.add_argument("--compare", action='store_true', help="Compare all algorithms on a map.")
    
import argparse
from environment import Environment
from agent import Agent

import time

def main():
    """
    Main function to run the autonomous delivery agent simulation.
    """
    parser = argparse.ArgumentParser(description="Autonomous Delivery Agent")
    parser.add_argument("map_file", help="Path to the map file.")
    parser.add_argument("--algorithm", choices=['bfs', 'ucs', 'a_star', 'local_search'], 
                        default='a_star', help="Search algorithm to use.")
    parser.add_argument("--dynamic", action='store_true', help="Demonstrate dynamic replanning.")
    parser.add_argument("--compare", action='store_true', help="Compare all algorithms on a map.")
    
    args = parser.parse_args()

    args = parser.parse_args()

    if args.compare:
        print(f"Comparing algorithms on map: {args.map_file}")
        algorithms_to_compare = ['bfs', 'a_star', 'local_search']
        results = []

        for algo_name in algorithms_to_compare:
            print(f"\n--- Running {algo_name.upper()} ---")
            try:
                env = Environment(args.map_file)
                agent = Agent(env)
                agent.set_algorithm(algo_name)
                
                print(f"Start position: {env.start_pos}")
                print(f"Goal position: {env.goal_pos}")
                
                start_time = time.perf_counter()
                path, nodes_expanded, cost = agent.find_path()
                end_time = time.perf_counter()
                
                time_taken = (end_time - start_time) * 1000 # in ms

                if path:
                    results.append({
                        "Algorithm": algo_name.upper(),
                        "Path Found": "Yes",
                        "Cost": f"{cost:.2f}",
                        "Nodes Expanded": nodes_expanded,
                        "Time (ms)": f"{time_taken:.4f}"
                    })
                else:
                    results.append({
                        "Algorithm": algo_name.upper(),
                        "Path Found": "No",
                        "Cost": "-",
                        "Nodes Expanded": nodes_expanded,
                        "Time (ms)": f"{time_taken:.4f}"
                    })

            except Exception as e:
                print(f"An error occurred while running {algo_name.upper()}: {e}")

        # Print summary table
        print("\n--- Comparison Results ---")
        if results:
            headers = results[0].keys()
            # Determine column widths
            widths = {h: max(len(str(h)), max(len(str(r[h])) for r in results)) for h in headers}
            # Print header
            header_line = " | ".join(h.ljust(widths[h]) for h in headers)
            print(header_line)
            print("-" * len(header_line))
            # Print rows
            for r in results:
                row_line = " | ".join(str(r[h]).ljust(widths[h]) for h in headers)
                print(row_line)

    else:
        # The existing logic for running a single algorithm or dynamic demo
        print(f"Loading map from: {args.map_file}")
        try:
            env = Environment(args.map_file)
        except FileNotFoundError:
            print(f"Error: Map file not found at '{args.map_file}'")
            return

        print(f"Start position: {env.start_pos}")
        print(f"Goal position: {env.goal_pos}")

        agent = Agent(env)
        try:
            agent.set_algorithm(args.algorithm)
        except ValueError as e:
            print(e)
            return

        print(f"Running with {args.algorithm.upper()} algorithm...")
        
        current_time_step = 0
        path, nodes_expanded, cost = agent.find_path(current_time_step=current_time_step)

        if not path:
            print("\nNo initial path found.")
            env.render(time_step=current_time_step)
            return

        print("\nInitial path found!")
        print(f"  - Nodes Expanded: {nodes_expanded}")
        print(f"  - Path Cost ({args.algorithm.upper()}): {cost}")
        print("\nInitial Grid with Path:")
        env.render(path=path, time_step=current_time_step)

        if args.dynamic:
            print("\n--- Dynamic Obstacle Simulation ---")
            
            # Simulate agent moving along the path
            simulated_path = []
            for i, pos in enumerate(path):
                simulated_path.append(pos)
                current_time_step += 1
                
                # Introduce dynamic obstacle at a specific point on the path
                if i == len(path) // 2:
                    obstacle_pos = path[i+1] # Obstacle appears one step ahead
                    obstacle_pos = (int(obstacle_pos[0]), int(obstacle_pos[1]))
                    print(f"\nA dynamic obstacle appears at {obstacle_pos} at time step {current_time_step}!")
                    # env.add_obstacle(obstacle_pos) # No longer needed as is_obstacle handles dynamic
                    
                    print("\nGrid with new obstacle:")
                    env.render(path=simulated_path, time_step=current_time_step) # Show current progress and new obstacle

                    print(f"\nAgent is at {pos}, replanning from time step {current_time_step}...")
                    
                    # Replan from the current position and time step
                    env.start_pos = pos # Agent's current position
                    new_path, new_nodes_expanded, new_cost = agent.find_path(current_time_step=current_time_step)

                    if not new_path:
                        print("\nCould not find a new path.")
                        env.render(time_step=current_time_step)
                        return

                    print("\nNew path found!")
                    print(f"  - Nodes Expanded: {new_nodes_expanded}")
                    print(f"  - Path Cost ({args.algorithm.upper()}): {new_cost}")
                    
                    # Combine the paths for rendering
                    final_path = simulated_path + new_path[1:] # Exclude current pos from new_path

                    print("\nFinal Grid with New Path:")
                    env.render(path=final_path, time_step=current_time_step)
                    return # End simulation after replanning demo

            print("\nAgent reached goal without dynamic obstacles.")
            env.render(path=path, time_step=current_time_step)


if __name__ == "__main__":
    main()
