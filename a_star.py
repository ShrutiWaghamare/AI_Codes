def heuristic(node):
    H_dist = {
        'A': 11, 'B': 6, 'C': 5, 'D': 7, 'E': 3,
        'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0
    }
    return H_dist[node]

Graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
}

def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    while open_set:
        current_node = min(open_set, key=lambda x: g[x] + heuristic(x))
        if current_node == stop_node:
            path = []
            while current_node != start_node:
                path.append(current_node)
                current_node = parents[current_node]
            path.append(start_node)
            path.reverse()
            return path

        open_set.remove(current_node)
        closed_set.add(current_node)

        for neighbor, weight in Graph_nodes.get(current_node, []):
            if neighbor in closed_set:
                continue

            if neighbor not in open_set or g[current_node] + weight < g[neighbor]:
                g[neighbor] = g[current_node] + weight
                parents[neighbor] = current_node
                if neighbor not in open_set:
                    open_set.add(neighbor)

    return None

path = aStarAlgo('A', 'J')
if path:
    print('Path found:', path)
else:
    print('Path does not exist!')
