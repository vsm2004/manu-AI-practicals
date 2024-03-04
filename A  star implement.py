import heapq

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def astar(graph, start, goal):
    frontier, came_from, cost_so_far = [(0, start)], {start: None}, {start: 0}
    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal: break
        for next_node in graph[current]:
            new_cost = cost_so_far[current] + graph[current][next_node]
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                heapq.heappush(frontier, (new_cost + heuristic(next_node, goal), next_node))
                came_from[next_node] = current
    path, current = [], goal
    while current != start: path.append(current); current = came_from[current]
    return path + [start]

if __name__ == "__main__":
    graph = {(0, 0): {(0, 1): 1, (1, 0): 1}, (0, 1): {(0, 0): 1, (1, 1): 1}, 
             (1, 0): {(0, 0): 1, (1, 1): 1}, (1, 1): {(0, 1): 1, (1, 0): 1}}
    start, goal = (0, 0), (1, 1)
    print("Path found:", astar(graph, start, goal))
