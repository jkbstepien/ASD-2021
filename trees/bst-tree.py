class BSTNode:
    """
    Class represents a single node of binary tree.
    """
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = value


class BSTree:
    """
    Class representing Binary Search Tree with it's
    operations.
    """
    def __init__(self, root=None):
        self.root = root

    def inorder(self, *args):
        """
        Produces list of nodes, obtained in inorder traversal.
        (Left, Root, Right)
        """
        if len(args) == 0:
            lst = []
            node = self.root
        else:
            node = args[0]
            lst = args[1]

        if node.left:
            self.inorder(node.left, lst)

        lst.append(node.key)

        if node.right:
            self.inorder(node.right, lst)

        return lst

    def preorder(self, *args):
        """
        Produces list of nodes, obtained in preorder traversal.
        (Root, Left, Right)
        """
        if len(args) == 0:
            lst = []
            node = self.root
        else:
            node = args[0]
            lst = args[1]

        lst.append(node.key)

        if node.left:
            self.inorder(node.left, lst)

        if node.right:
            self.inorder(node.right, lst)

        return lst

    def postorder(self, *args):
        """
        Produces list of nodes, obtained in postorder traversal.
        (Left, Right, Root)
        """
        if len(args) == 0:
            lst = []
            node = self.root
        else:
            node = args[0]
            lst = args[1]

        if node.left:
            self.inorder(node.left, lst)

        if node.right:
            self.inorder(node.right, lst)

        lst.append(node.key)

        return lst

    def get_height(self, *args):
        """
        Obtain height of binary tree. Root + highest subtree.
        """
        if len(args) == 0:
            node = self.root
        else:
            node = args[0]

        if not node:
            return 0
        elif not node.left and not node.right:
            return 1
        else:
            return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def find(self, key, *args):
        """
        Find node in binary tree with key attribute key.
        """
        if len(args) == 0:
            start = self.root
        else:
            start = args[0]

        if not start:
            return None
        if start.key == key:
            return start
        elif start.key < key:
            return self.find(key, start.right)
        else:
            return self.find(key, start.left)

    def insert(self, key, value, *args):
        """
        Inserts a new node with key attribute key and value
        attribute value into binary tree.
        """
        if not self.root:
            self.root = BSTNode(key, value)
        elif len(args) == 0:
            if not self.find(key, self.root):
                self.insert(key, value, self.root)
        else:
            to_add = BSTNode(key, value)
            parent = args[0]
            if to_add.key < parent.key:
                if not parent.left:
                    parent.left = to_add
                    to_add.parent = parent
                else:
                    self.insert(key, value, parent.left)
            else:
                if not parent.right:
                    parent.right = to_add
                    to_add.parent = parent
                else:
                    self.insert(key, value, parent.right)

    def get_min(self, *args):
        """
        Obtain from binary tree a node with min key.
        """
        if len(args) == 0:
            start = self.root
        else:
            start = args[0]

        if start.left:
            return self.get_min(start.left)
        else:
            return start

    def get_max(self, *args):
        """
        Obtain from binary tree a node with max key.
        """
        if len(args) == 0:
            start = self.root
        else:
            start = args[0]

        if start.right:
            return self.get_max(start.right)
        else:
            return start

    @staticmethod
    def delete_leaf(node):
        """
        Deletes node in binary tree, leaf case.
        """
        parent_node = node.parent

        if parent_node:
            if parent_node.left == node:
                parent_node.left = None
            else:
                parent_node.right = None

    def delete_one_child(self, node):
        """
        Deletes node in binary tree, which has one child.
        """
        parent_node = node.parent

        if node.key == self.root.key:
            if node.right:
                self.root = node.right
                node.right = None
            else:
                self.root = node.left
                node.left = None
        else:
            if parent_node.right == node:
                # Removing right node with one child.
                if node.left:
                    parent_node.right = node.left
                    parent_node.right.parent = parent_node
                    node.left = None
                else:
                    parent_node.right = node.right
                    parent_node.right.parent = parent_node
                    node.right = None
            else:
                # Removing left node with one child.
                if node.left:
                    parent_node.left = node.left
                    parent_node.left.parent = parent_node
                    node.left = None
                else:
                    parent_node.left = node.right
                    parent_node.left.parent = parent_node
                    node.right = None

    def swap_nodes(self, node1, node2):
        """
        Swap positions of node1 and node2.
        """
        swap_1 = node1
        swap_2 = node2
        tmp_key = swap_1.key
        tmp_val = swap_1.value

        if swap_1.key == self.root.key:
            self.root.key = swap_2.key
            self.root.value = swap_2.value
            swap_2.key = tmp_key
            swap_2.value = tmp_val
        elif swap_2.key == self.root.key:
            swap_1.key = self.root.key
            self.root.key = tmp_key
            self.root.value = tmp_val
        else:
            swap_1.key = node2.key
            swap_1.value = node2.value
            swap_2.key = tmp_key
            swap_2.value = tmp_val

    def delete_two_children(self, node):
        """
        Deletes node in binary tree, which has two children.
        """
        if self.get_height(node.left) > self.get_height(node.right):
            to_swap = self.get_max(node.left)
            self.swap_nodes(node, to_swap)

            if not to_swap.right and not to_swap.left:
                to_remove = self.get_max(node.left)
                self.delete_leaf(to_remove)
            else:
                to_remove = self.get_max(node.left)
                self.delete_one_child(to_remove)
        else:
            to_swap = self.get_min(node.right)
            self.swap_nodes(node, to_swap)

            if not to_swap.right and not to_swap.left:
                to_remove = self.get_min(node.right)
                self.delete_leaf(to_remove)
            else:
                to_remove = self.get_min(node.right)
                self.delete_one_child(to_remove)

    def delete(self, key):
        """
        Delete the node from binary tree with key attribute key.
        """
        node = self.find(key, self.root)

        if node:
            if not node.left and not node.right:
                self.delete_leaf(node)
            elif not (node.left and node.right):
                self.delete_one_child(node)
            else:
                self.delete_two_children(node)


def main():
    # Tests
    tree = BSTree()
    tree.insert(10, None)
    tree.insert(5, None)
    tree.insert(2, None)
    tree.insert(7, None)
    tree.insert(9, None)
    tree.insert(20, None)
    print(tree.inorder())
    print(tree.preorder())
    print(tree.postorder())
    print(f"min: {tree.get_min().key}")
    print(f"max: {tree.get_max().key}")
    print(f"tree height: {tree.get_height()}")
    tree.delete(5)
    print(tree.inorder())


if __name__ == "__main__":
    main()
