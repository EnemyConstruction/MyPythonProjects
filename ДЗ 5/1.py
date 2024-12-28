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

    def average(self):
        total_sum, count = self.count_sum(self.root)
        return total_sum / count if count > 0 else 0

    def count_sum(self, node):
        if node is None:
            return 0, 0
        left_sum, left_count = self.count_sum(node.left)
        right_sum, right_count = self.count_sum(node.right)
        total_sum = left_sum + right_sum + node.value
        total_count = left_count + right_count + 1
        return total_sum, total_count

    def tree_order(self):
        values = []
        self.full_tree(self.root, values)
        print("Вершины дерева:", values)

    def full_tree(self, node, values):
        if node is not None:
            self.full_tree(node.left, values)
            values.append(node.value)
            self.full_tree(node.right, values)

tree = BinaryTree()

tree.insert(10.8)
tree.insert(6.03)
tree.insert(-3)
tree.insert(2)
tree.insert(56)

average_value = tree.average()
print(f"Среднее арифметическое вершин: {average_value}")

tree.insert(average_value)
print(f"В дерево добавлено значение {average_value}")

tree.tree_order()