#%% Imports and functions declarations
from collections import deque


class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)


def bfs_search(root_node, search_value):
    seen_nodes = list()
    queue = deque()

    node = root_node
    node_value = node.value

    if node_value == search_value:
        return node

    seen_nodes.append(node_value)
    first_loop = True

    while (len(queue) > 0) or first_loop:
        first_loop = False

        for node_children in node.children:  # Visit all the current level
            if node_children.value not in seen_nodes:
                node_value = node_children.value

                if node_value == search_value:
                    return node_children

                seen_nodes.append(node_value)
                queue.append(node_value)

        next_node_value = queue.popleft()

        for node_children in node.children:  # Move to next node
            if node_children.value is next_node_value:
                node = node_children
                first_loop = True
                break

    return -1


#%% Data construction
nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS, nodeH, nodeG, nodeP, nodeR, nodeA])
graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeA, nodeR)
graph1.add_edge(nodeA, nodeG)
graph1.add_edge(nodeR, nodeP)
graph1.add_edge(nodeH, nodeG)
graph1.add_edge(nodeH, nodeP)
graph1.add_edge(nodeS, nodeR)


#%% Test - Development
assert nodeA == bfs_search(nodeS, 'A')
assert nodeS == bfs_search(nodeP, 'S')
assert nodeR == bfs_search(nodeH, 'R')
