from queue import PriorityQueue
def best_first_search(graph, start, goal):
    queue = PriorityQueue()
    queue.put((0, start))
    visited = set()
    while not queue.empty():
        _, current_node = queue.get()
        if current_node == goal:
            return True
        visited.add(current_node)
        for neighbor in graph.get(current_node, []):  # Ensure neighbor exists in the graph
            if neighbor not in visited:
                queue.put((len(visited), neighbor))  # Adjusted to prioritize based on number of visited nodes
    return False
if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
    start, goal = 'A', 'F'
    print("Path exists:", best_first_search(graph, start, goal))
