def color_map(graph, colors):
    colored_map = {}
    for region in graph:
        available_colors = set(colors)
        for neighbor in graph[region]:
            if neighbor in colored_map:
                available_colors.discard(colored_map[neighbor])
        colored_map[region] = next(iter(available_colors))
    return colored_map

graph = {
    'A': {'B', 'C', 'D'},
    'B': {'A', 'C'},
    'C': {'A', 'B', 'D'},
    'D': {'A', 'C'}
}
colors = ['Red', 'Green', 'Blue']

print(color_map(graph, colors))
