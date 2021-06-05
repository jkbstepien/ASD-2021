"""
zad obowiązkowe - operacje na BST.
"""

class BSTNode:
    """
    Class represents a single node in BST tree.
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def tree_find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif root.key > key:
            root = root.left
        else:
            root = root.right

    return None


def tree_insert(root, key):
    prev = None
    while root is not None:
        prev = root
        if key < root.key:
            root = root.left
        else:
            root = root.right

    if prev is None:
        # Tree is empty.
        root = BSTNode(key)
    elif key < prev.key:
        prev.left = BSTNode(key)
        prev.left.parent = prev
    else:
        prev.right = BSTNode(key)
        prev.right.parent = prev


def tree_remove_node(root, key):
    if root is None:
        return root

    if root.key > key:
        root.left = tree_remove_node(root.left, key)
    elif root.key < key:
        root.right = tree_remove_node(root.right, key)
    else:
        # No child or only one child.
        if root.left is None and root.right is None:
            if root.key == key:
                root = None
                return
            par = root.parent
            if par.left == root:
                par.left = None
            else:
                par.right = None
            return root
        elif root.left is None:
            if root.key == key:
                root = root.right
                return root
            par = root.parent
            if par.left == root:
                par.left = root.right
            else:
                par.right = root.right
            return root
        elif root.right is None:
            if root.key == key:
                root = root.left
                return root
            par = root.parent
            if par.left == root:
                par.left = root.left
            else:
                par.right = root.left
            return root
        else:
            # Two children.
            a = tree_min(root.right)
            root.key = a
            root.right = tree_remove_node(root.right, a)

    return root


def tree_min(root):
    prev = None
    while root is not None:
        prev = root
        root = root.left

    return prev.key


def tree_max(root):
    prev = None
    while root is not None:
        prev = root
        root = root.right

    return prev.key


def tree_predecessor(node):
    x = node
    if x.left is not None:
        return tree_max(x.left)

    y = x.parent
    while y is not None and x == y.left:
        x = y
        y = y.parent
    if y is None:
        return None

    return y.key


def tree_successor(node):
    x = node
    if x is None:
        return None
    if x.right is not None:
        return tree_min(x.right)

    y = x.parent
    while y is not None and x == y.right:
        x = y
        y = y.parent
    if y is None:
        return None

    return y.key


def inorder(root, res):
    # Recursive traversal
    if root:
        inorder(root.left, res)
        res.append(root.key)
        inorder(root.right, res)
    return res


if __name__ == "__main__":

    nodes = [20, 10, 5, 15, 13, 27, 22, 30, 28, 35, 40]
    root = BSTNode(20)
    tree_insert(root, 10)
    tree_insert(root, 5)
    tree_insert(root, 15)
    tree_insert(root, 13)
    tree_insert(root, 27)
    tree_insert(root, 22)
    tree_insert(root, 30)
    tree_insert(root, 28)
    tree_insert(root, 35)
    tree_insert(root, 40)
    print(inorder(root, []))
    print(tree_predecessor(tree_find(root, 20)))

    print("\nRemoving each node in a tree.")
    for node in nodes:
        root = tree_remove_node(root, node)
        print(inorder(root, []))
