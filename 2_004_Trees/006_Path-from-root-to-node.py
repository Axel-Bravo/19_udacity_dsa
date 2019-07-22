#%% Imports and function declaration
from queue import Queue

class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def convert_arr_to_binary_tree(arr):
    """
    Takes arr representing level-order traversal of Binary Tree
    """
    index = 0
    length = len(arr)

    if length <= 0 or arr[0] == -1:
        return None

    root = BinaryTreeNode(arr[index])
    index += 1
    queue = Queue()
    queue.put(root)

    while not queue.empty():
        current_node = queue.get()
        left_child = arr[index]
        index += 1

        if left_child is not None:
            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            queue.put(left_node)

        right_child = arr[index]
        index += 1

        if right_child is not None:
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            queue.put(right_node)
    return root


def path_from_root_to_node(root, data):
    """
    :param: root - root of binary tree
    :param: data - value (representing a node)
    from root to the data node
    """
    if root.data == data:  # Value found
        return [data]

    if (root.left is None) and (root.right) is None:  # Not found in this branch and no more depth
        return []

    left_findings = [root.data]
    right_findings = [root.data]

    if root.left is not None:
        left_findings.extend(path_from_root_to_node(root.left, data))

    if root.right is not None:
        right_findings.extend(path_from_root_to_node(root.right, data))

    if len(left_findings) > 1:
        return left_findings
    elif len(right_findings) > 1:
        return right_findings
    else:
        return []


#%% Testing
arr = [1, 2, 3, 4, 5, None, None, None, None, None, None]
data = 5
solution = [1, 2, 5]
bin_tree = convert_arr_to_binary_tree(arr)
print(path_from_root_to_node(bin_tree, data))

arr = [1, 2, 3, 4, None, 5, None, None, None, None, None]
data = 5
solution = [1, 3, 5]
bin_tree = convert_arr_to_binary_tree(arr)
print(path_from_root_to_node(bin_tree, data))

arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
data = 11
solution = [1, 3, 4, 6, 10, 11]
bin_tree = convert_arr_to_binary_tree(arr)
print(path_from_root_to_node(bin_tree, data))

arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
data = 8
solution = [1, 3, 5,8]
bin_tree = convert_arr_to_binary_tree(arr)
print(path_from_root_to_node(bin_tree, data))
