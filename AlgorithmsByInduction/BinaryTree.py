class TreeNode:
    def __init__(self, i):
        self.data = i
        self.left:TreeNode = None
        self.right:TreeNode = None

class BinaryTree:
    def __init__(self, node:TreeNode = None):
        if node:
            self.root = node
        else:
            self.root = None

    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False