class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.count_elem = 1


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
        prev.count_elem += 1
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


def find_ith(tree, elem_idx):
    node = tree.root
    # Check if elem_idx is in tree range.
    if elem_idx > node.count_elem:
        return -1

    while node.right is not None or node.left is not None:
        # Check if we are in the right place in a tree.
        if node.left is not None and node.left.count_elem + 1 == elem_idx:
            return node.key
        # Otherwise check if we can go to left branch.
        elif node.left is not None and node.left.count_elem >= elem_idx:
            node = node.left
        else:
            # If not any of the above, try to go right and decrease
            # index of element by how many nodes we've passed.
            if node.left is not None:
                elem_idx -= node.left.count_elem
            node = node.right
            elem_idx -= 1

    return node.key


if __name__ == "__main__":
    T = BSTree()
    print("INSERTING")
    for v in [32, 3, 21, 16, 1, 20, 38, 35, 6, 4]:
        print(v, insert(T, v))
    for i in range(1, 11):
        print(i, ":", find_ith(T, i))
