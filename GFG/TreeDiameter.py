#https://www.geeksforgeeks.org/problems/diameter-of-binary-tree/1

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def diameter(self, root):
        # Your code here

        if root == None:
            return 0

        def height(node):
            
            if node == None:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            nonlocal res
            res = max(res, left_height + right_height)
            
            return max(left_height, right_height) + 1
        

        res = 0
        height(root)
        return res
        

root = Node(1)
root.left = Node(2)
root.left.left = Node(2)
root.right = Node(3)

s=Solution()
print(s.diameter(root))