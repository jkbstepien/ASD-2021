class BSTNode:
    """
    Class represents a single node of binary tree.
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BSTree:
    def __init__(self):
        self.root = None


def insert(tree, key):
    root = tree.root
    if root is None:
        tree.root = BSTNode(key)
        return True

    prev = None
    while root is not None:
        if root.key == key:
            return False
        prev = root
        if root.key < key:
            root = root.right
        else:
            root = root.left

    new = BSTNode(key)
    if prev.key < key:
        prev.right = new
    else:
        prev.left = new
    new.parent = prev

    return True


def sum_bst(root):
    """
    Obtain sum of all elements in binary search tree.
    """
    if root is None:
        return 0
    root.key += sum_bst(root.left) + sum_bst(root.right)

    return root.key


def restore_bst(root):
    """
    Restore binary search tree to it's previous condition.
    """
    if root.left is not None:
        root.key -= root.left.key
        restore_bst(root.left)
    if root.right is not None:
        root.key -= root.right.key
        restore_bst(root.right)


def inorder(root, res):
    # Recursive traversal
    if root:
        inorder(root.left, res)
        res.append(root.key)
        inorder(root.right, res)
    return res


if __name__ == "__main__":
    tree = BSTree()
    for v in [10, 5, 2, 7, 9, 20]:
        insert(tree, v)

    # At first we call sum_bst, then restore_bst.
    res = sum_bst(tree.root)
    if res == 53:
        print("sum is correct")
    else:
        print("ERROR")

    print(f"after modification: {inorder(tree.root, [])}")
    restore_bst(tree.root)
    print(f"restored tree: {inorder(tree.root, [])}")
