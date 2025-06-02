class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def findMaxFork(self, root, k):
        #code here

        # Approach => Recursive
        # TC => h
        # SC => h

        # max_k = 0
        #
        # def recur(node):
        #
        #     if node == None:
        #        return
        #
        #     if node.data <= k:
        #         nonlocal max_k
        #         max_k = node.data
        #         recur(node.right)
        #     else:
        #         recur(node.left)
        #
        # recur(root)
        # return max_k

        # Approach 2: iterative
        result = -1
        while root:

            if root.data <= k:
                result = root.data
                root = root.right
            else:
                root = root.left

        return  result
s=Solution()
root = Node(5)
root.left = Node(2)
root.right = Node(12)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(9)
root.right.right = Node(21)
root.right.right.left = Node(19)
root.right.right.right = Node(25)
print(s.findMaxFork(root, 4))