"""
Jakub Stępień
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

    def checkIntegrity(self) -> None:
        '''Sprawdza czy kazde dziecko ma przypisanego parenta(czy drzewo jest dobrze zrobione)'''
        if self.left != None:
            assert self.left.parent == self
            self.left.checkIntegrity()
        if self.right != None:
            assert self.right.parent == self
            self.right.checkIntegrity()

    def __str__(self) -> str:
        ret = ""
        if self.left != None:
            ret += str(self.left) + "<"
        ret += str(self.key)
        if self.right != None:
            ret += "<" + str(self.right)
        return ret


def tree_find(root, key): # git
    while root is not None:
        if root.key == key:
            return root
        elif root.key > key:
            root = root.left
        else:
            root = root.right

    return None


def tree_insert(leaf, key): # nie git
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

def delete_root(leaf):

    # No child or only one child.
    if leaf.left is None and leaf.right is None:  # git
        return None
    elif leaf.left is None:  # prawy istnieje git
        leaf.right.parent = None
        return leaf.right
    elif leaf.right is None:  # lewy istnieje
        leaf.left.parent = None
        return leaf.left
    else:  # git
        # Two children.
        a = tree_min(leaf.right)
        leaf.key = a.key
        tree_remove_node(a, a.key)

    return leaf


def delete(leaf, key):
    if leaf is None:
        return False,leaf
    if leaf.key == key:
        leaf = delete_root(leaf)
        return True,leaf
    else:
        ret = tree_remove_node(leaf,key)
        return ret,leaf

def tree_remove_node(leaf, key):
    if leaf is None:
        return False

    if leaf.key > key:
        return tree_remove_node(leaf.left, key)
    elif leaf.key < key:
        return tree_remove_node(leaf.right, key)
    else:
        # No child or only one child.
        if leaf.left is None and leaf.right is None:  # git
            par = leaf.parent
            if par.left == leaf:
                par.left = None
            else:
                par.right = None
            return True
        elif leaf.left is None:  # prawy istnieje git
            par = leaf.parent
            leaf.right.parent = leaf.parent
            if par.left == leaf:
                par.left = leaf.right
            else:
                par.right = leaf.right
            return True
        elif leaf.right is None:  # lewy istnieje
            par = leaf.parent
            leaf.left.parent = leaf.parent
            if par.left == leaf:
                par.left = leaf.left
            else:
                par.right = leaf.left
            return True
        else:  # git
            # Two children.
            a = tree_min(leaf.right)
            leaf.key = a.key
            tree_remove_node(a, a.key)

    return True


def tree_min(leaf):
    while leaf.left is not None:
        leaf = leaf.left
    return leaf


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
    from random import randint
    root = BSTNode(123)
    secior = set()
    for i in range(500):
        a = randint(0, 550)
        secior.add(a)
        ret, root = tree_insert(root,a)
        if root != None:
            root.checkIntegrity()
    for elem in secior:
        ret, root = delete(root, elem)
        assert ret == True
        print(root)
        # print(inorder(root,[]))
        if root != None:
            root.checkIntegrity()


    # nodes = [20, 10, 5, 15, 13, 27, 22, 30, 28, 35, 40]
    # root = BSTNode(20)
    # for elem in nodes:
    #     ret, root = tree_insert(root,elem)
    #
    # print(root)
    # print(tree_predecessor(root))
    #
    # print("\nRemoving each node in a tree.")
    # for node in nodes:
    #     ret, root = delete(root, node)
    #     print(root)

