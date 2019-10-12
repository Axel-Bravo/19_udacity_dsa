def path_from_root_to_node(root, data):
    """
    Assuming data as input to find the node
    The solution can be easily changed to find a node instead of data
    :param data:
    :return:
    """
    output = path_from_node_to_root(root, data)
    return list(reversed(output))

def path_from_node_to_root(root, data):
    if root is None:
        return None

    elif root.data == data:
        return [data]

    left_answer = path_from_node_to_root(root.left, data)
    if left_answer is not None:
        left_answer.append(root.data)
        return left_answer

    right_answer = path_from_node_to_root(root.right, data)
    if right_answer is not None:
        right_answer.append(root.data)
        return right_answer
    return None