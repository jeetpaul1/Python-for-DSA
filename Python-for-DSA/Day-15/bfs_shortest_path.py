#Write a Python program to implement BFS on a graph and find the shortest path between a source and a target node.


from collections import deque  #solution

def bfs_shortest_path(graph, start, target):
    """
    Perform BFS to find the shortest path from start to target.

    Args:
        graph (dict): The graph represented as an adjacency list.
        start (str): The starting node.
        target (str): The target node.

    Returns:
        list: The shortest path from start to target, or an empty list if no path exists.
    """
    # Queue to hold (current_node, path_to_node)
    queue = deque([(start, [start])])
    visited = set()  # Track visited nodes

    while queue:
        current, path = queue.popleft()

        if current == target:
            return path  # Found the target, return the path

        visited.add(current)  # Mark the current node as visited

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))  # Add neighbor and updated path to queue

    return []  # No path found

# Example usage
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

start_node = "A"
target_node = "F"

shortest_path = bfs_shortest_path(graph, start_node, target_node)
print(f"Shortest path from {start_node} to {target_node}: {shortest_path}")
