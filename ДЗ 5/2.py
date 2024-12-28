class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.recursion_insert(self.root, value)

    def recursion_insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.recursion_insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.recursion_insert(node.right, value)

    def tree_order(self):
        values = []
        self.full_tree(self.root, values)
        print("Вершины дерева:", values)

    def full_tree(self, node, values):
        if node is not None:
            self.full_tree(node.left, values)
            values.append(node.value)
            self.full_tree(node.right, values)

    def make_type(self, node):
        if node is None:
            return None
        if node == self.root:
            return 'К' 
        elif node.left is None and node.right is None:
            return 'Л' 
        else:
            return 'П' 

    def print_types(self):
        types = []
        self.take_types(self.root, types)
        print("Типы всех вершин дерева:", types)

    def take_types(self, node, types):
        if node is not None:
            types.append((node.value, self.make_type(node)))
            self.take_types(node.left, types)
            self.take_types(node.right, types)

tree = BinaryTree()

tree.insert(10.8)
tree.insert(6.03)
tree.insert(-3)
tree.insert(2)
tree.insert(56)

tree.tree_order()
tree.print_types()