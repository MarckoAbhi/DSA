class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def insert(self, value):
        self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left:
                self._insert(current.left, value)
            else:
                current.left = TreeNode(value)
        else:
            if current.right:
                self._insert(current.right, value)
            else:
                current.right = TreeNode(value)

    def display(self):
        self._display(self.root)

    def _display(self, current):
        if current:
            self._display(current.left)
            print(current.value, end=" ")
            self._display(current.right)
