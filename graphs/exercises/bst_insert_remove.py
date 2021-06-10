"""
Offline nr 11.
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


"""Funkcja do dodawania węzłów do drzewa."""
def insert(leaf, key) -> (bool, BSTNode):
    root_cpy = leaf
    prev = None
    while leaf is not None:
        prev = leaf
        if key < leaf.key:
            leaf = leaf.left
        elif key == leaf.key:
            return False, root_cpy
        else:
            leaf = leaf.right

    if prev is None:
        # Tree is empty.
        root_cpy = BSTNode(key)
    elif key < prev.key:
        prev.left = BSTNode(key)
        prev.left.parent = prev
    else:
        prev.right = BSTNode(key)
        prev.right.parent = prev

    return True, root_cpy


# Usuwanie w zaleznosci czy jest to root czy inny wezel/lisc
# zwracam wartosci (czy udalo sie usunac, root po usunieciu) bo roota trzeba zwracac
def delete(leaf, key) -> (bool, BSTNode):
    if leaf is None:
        return False, None
    if leaf.key == key:
        leaf = delete_root(leaf)
        return True, leaf
    else:
        ret = tree_remove_node(leaf,key)
        return ret, leaf


def tree_remove_node(leaf, key):
    if leaf is None:
        return False

    if leaf.key > key:
        return tree_remove_node(leaf.left, key)
    elif leaf.key < key:
        return tree_remove_node(leaf.right, key)
    else:
        if leaf.left is None and leaf.right is None:  # zadne dziecko nie istnieje
            par = leaf.parent
            if par.left == leaf:
                par.left = None
            else:
                par.right = None
            return True
        elif leaf.left is None:  # prawe dziecko isnieje
            par = leaf.parent
            leaf.right.parent = leaf.parent
            if par.left == leaf:
                par.left = leaf.right
            else:
                par.right = leaf.right
            return True
        elif leaf.right is None:  # lewe dziecko istnieje
            par = leaf.parent
            leaf.left.parent = leaf.parent
            if par.left == leaf:
                par.left = leaf.left
            else:
                par.right = leaf.left
            return True
        else:
            # Dwojka dzieci
            a = tree_min(leaf.right)
            leaf.key = a.key
            tree_remove_node(a, a.key)

    return True

def delete_root(leaf):
    if leaf.left is None and leaf.right is None:  # zadne dziecko nie istnieje
        return None
    elif leaf.left is None:  # prawe dziecko isnieje
        leaf.right.parent = None
        return leaf.right
    elif leaf.right is None:  # lewe dziecko istnieje
        leaf.left.parent = None
        return leaf.left
    else:  # dwojka dzieci
        a = tree_min(leaf.right)
        leaf.key = a.key
        tree_remove_node(a, a.key)

    return leaf

def tree_min(leaf):
    while leaf.left is not None:
        leaf = leaf.left
    return leaf
