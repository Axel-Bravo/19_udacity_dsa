#%% Imports and function declaration
from queue import Queue

class BinaryTreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


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


def diameter_of_binary_tree(root):
    """
    :param: root - Root of binary tree
    """

    if root is None:
        return 0

    else:
        return sum(_diameter_binary_rec(root))


def _diameter_binary_rec(root):
    node = root
    left_depth = 0
    right_depth = 0

    if root is None:
        return 0

    if node.left is not None:
        left_depth = max(_diameter_binary_rec(node.left)) + 1

    if node.right is not None:
        right_depth = max(_diameter_binary_rec(node.right)) + 1

    return [left_depth, right_depth]


#%% Testing
arr = [1, 2, 3, 4, 5, None, None, None, None, None, None]
solution = 3
bin_tree = convert_arr_to_binary_tree(arr)
print(diameter_of_binary_tree(bin_tree))

arr = [1, 2, 3, 4, None, 5, None, None, None, None, None]
solution = 4
bin_tree = convert_arr_to_binary_tree(arr)
print(diameter_of_binary_tree(bin_tree))

arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
solution = 6
bin_tree = convert_arr_to_binary_tree(arr)
print(diameter_of_binary_tree(bin_tree))

