#%% Imports and functions declarations
import heapq


def adjacent_graph(num_islands: int, bridge_config: list) -> list:
    """
    Transforms a bridge configuration into an adjacent graph list
    :param num_islands: number of islands
    :param bridge_config: bridge connection configuration list
    :return: graph in adjancent format
    """
    graph_adjacents = [ [] for _ in range(num_islands + 1)]  # To have the same index as the islands, skip 0

    for bridge in bridge_config:
        left_side = bridge[0]
        right_side = bridge[1]
        conn_cost = bridge[2]

        graph_adjacents[left_side].append((right_side, conn_cost))
        graph_adjacents[right_side].append((left_side, conn_cost))

    return graph_adjacents


def min_connections(graph: list) -> int:
    """
    Given a graph in adjacent format, informs about the minimal cost to have all islands connected by bridges
    :param graph: graph in adjacent format list
    :return: minimum cost of connection
    """
    nodes_visited = [False for _ in range(len(graph) + 1)]
    connection_cost = 0

    initial_node = 1
    connections = [(0, initial_node)]

    while len(connections) > 0:
        cost, current_node = heapq.heappop(connections)

        if nodes_visited[current_node]:
            continue
        else:
            connection_cost += cost

            for neighbor, node_cost in graph[current_node]:
                heapq.heappush(connections, (node_cost, neighbor))

            nodes_visited[current_node] = True

    return connection_cost


#%%% Test - Development
num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6
assert solution == min_connections(adjacent_graph(num_islands, bridge_config)), 'Error on program implementation'

num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13
assert solution == min_connections(adjacent_graph(num_islands, bridge_config)), 'Error on program implementation'

num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31
assert solution == min_connections(adjacent_graph(num_islands, bridge_config)), 'Error on program implementation'
