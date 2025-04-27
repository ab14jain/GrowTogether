class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None

# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Code here

        def mirror(node):

            if node == None:
                return
            
            mirror(node.left)
            mirror(node.right)
            left = node.left
            node.left = node.right
            node.right = left

        mirror(root)
        return root
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)

s = Solution()
rt = s.mirror(root)