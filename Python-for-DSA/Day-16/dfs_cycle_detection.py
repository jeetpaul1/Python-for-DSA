#Write a Python program to implement DFS and detect if a given undirected graph contains a cycle.


def dfs_cycle_detection(graph, node, visited, parent): #solution
    """
    Perform DFS to detect a cycle in an undirected graph.

    Args:
        graph (dict): The graph represented as an adjacency list.
        node (str): The current node being visited.
        visited (set): A set of visited nodes.
        parent (str): The parent node of the current node.

    Returns:
        bool: True if a cycle is detected, False otherwise.
    """
    visited.add(node)  # Mark the current node as visited

    for neighbor in graph.get(node, []):
        if neighbor not in visited:  # If the neighbor is not visited, recurse
            if dfs_cycle_detection(graph, neighbor, visited, node):
                return True
        elif neighbor != parent:  # If the neighbor is visited and not the parent, a cycle exists
            return True

    return False

def has_cycle(graph):
    """
    Check if the given undirected graph contains a cycle.

    Args:
        graph (dict): The graph represented as an adjacency list.

    Returns:
        bool: True if a cycle exists, False otherwise.
    """
    visited = set()
    for node in graph:
        if node not in visited:  # Perform DFS for unvisited nodes
            if dfs_cycle_detection(graph, node, visited, None):
                return True
    return False

# Example usage
graph_with_cycle = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

graph_without_cycle = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B"]
}

print("Graph with cycle:", has_cycle(graph_with_cycle))  # True
print("Graph without cycle:", has_cycle(graph_without_cycle))  # False
