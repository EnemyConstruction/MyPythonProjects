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

    def max(self):
        if not self.root:
            return None
        return self.recursion_max(self.root)

    def recursion_max(self, current_node):
        while current_node.right:
            current_node = current_node.right
        return current_node.value

    def min(self):
        if not self.root:
            return None
        return self.recursion_min(self.root)

    def recursion_min(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value

    def leaves(self):
        leaves = []
        self.take_leaves(self.root, leaves)
        print("Листья дерева:", leaves)

    def take_leaves(self, current_node, leaves):
        if current_node:
            if not current_node.left and not current_node.right:
                leaves.append(current_node.value)
            self.take_leaves(current_node.left, leaves)
            self.take_leaves(current_node.right, leaves)

tree = BinaryTree()

tree.insert(10.8)
tree.insert(6.03)
tree.insert(-3)
tree.insert(2)
tree.insert(56)

max_value = tree.max()
min_value = tree.min()
print(f"Максимальное значение: {max_value}")
print(f"Минимальное значение: {min_value}")

tree.leaves()