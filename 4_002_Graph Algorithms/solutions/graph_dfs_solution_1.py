def dfs_search(root_node, search_value):
    visited = []
    stack = [root_node]
    
    while len(stack) > 0:
        current_node = stack.pop()
        visited.append(current_node)

        if current_node.value == search_value:
            return current_node

        for child in current_node.children:
            if child not in visited:
                stack.append(child)