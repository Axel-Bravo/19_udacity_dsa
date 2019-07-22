#%% Imports and function declaration


class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


# Personal implementations
def pre_order(tree: Tree):
    """
    Traverse first the node, then the left side and later the right side
    """
    return pre_order_dfs(tree.get_root())


def pre_order_dfs(node: Node):

    if (not node.has_left_child()) and (not node.has_right_child()):  # We reached a leaf
        return [node.get_value()]

    lvl_visited = [node.get_value()]  # First time we visit the node, it is saved

    if node.has_left_child():
        lvl_visited.extend(pre_order_dfs(node.get_left_child()))  # Traverse left node

    if node.has_right_child():
        lvl_visited.extend(pre_order_dfs(node.get_right_child()))  # Traverse right node

    return lvl_visited


def in_order(tree: Tree):
    """
    Traverse the left subtree, then visit the node, and then traverse the right subtree.
    """
    return in_order_dfs(tree.get_root())


def in_order_dfs(node: Node):

    if (not node.has_left_child()) and (not node.has_right_child()):  # We reached a leaf
        return [node.get_value()]

    lvl_visited = []

    if node.has_left_child():
        lvl_visited.extend(in_order_dfs(node.get_left_child()))  # Traverse left node

    lvl_visited.extend([node.get_value()])  # First time we visit the node, it is saved

    if node.has_right_child():
        lvl_visited.extend(in_order_dfs(node.get_right_child()))  # Traverse right node

    return lvl_visited


def post_order(tree: Tree):
    """
    Traverse left subtree, then right subtree, and then visit the node.
    """
    return post_order_dfs(tree.get_root())


def post_order_dfs(node: Node):

    if (not node.has_left_child()) and (not node.has_right_child()):  # We reached a leaf
        return [node.get_value()]

    lvl_visited = []

    if node.has_left_child():
        lvl_visited.extend(post_order_dfs(node.get_left_child()))  # Traverse left node

    if node.has_right_child():
        lvl_visited.extend(post_order_dfs(node.get_right_child()))  # Traverse right node

    lvl_visited.extend([node.get_value()])  # First time we visit the node, it is saved

    return lvl_visited

#%% Testing
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

test = post_order(tree=tree)