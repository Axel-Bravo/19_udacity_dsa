def dijkstra(start_node, end_node):
    distance_dict = {node: math.inf for node in graph.nodes}
    shortest_path_to_node = {}

    distance_dict[start_node] = 0
    while distance_dict:
        # Pop the shorest path 
        current_node, node_distance = sorted(distance_dict.items(), key=lambda x: x[1])[0]
        shortest_path_to_node[current_node] = distance_dict.pop(current_node)

        for edge in current_node.edges:
            if edge.node in distance_dict:
                new_node_distance = node_distance + edge.distance
                if distance_dict[edge.node] > new_node_distance:
                    distance_dict[edge.node] = new_node_distance
    
    return shortest_path_to_node[end_node]