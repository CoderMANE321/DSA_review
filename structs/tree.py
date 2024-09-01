from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert a new node and return the root of the BST.
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return self.root

        def _insert(node, val):
            if not node:
                return TreeNode(val)
            if val > node.val:
                node.right = _insert(node.right, val)
            elif val < node.val:
                node.left = _insert(node.left, val)
            return node

        _insert(self.root, val)
        return self.root

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val)
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.val)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val)

    def bfs(self, node):
        queue = deque()

        if node:
            queue.append(node)

        level = 0
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()
                print(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1


"""
use

from structs.tree import BinaryTree

t = BinaryTree()

t.insert(10)
t.insert(20)
t.insert(9)
t.insert(5)
t.insert(3)
t.insert(26)
t.insert(30)

t.inorder(t.root)
t.preorder(t.root)
t.postorder(t.root)
t.bfs(t.root)
print(t.root)
"""