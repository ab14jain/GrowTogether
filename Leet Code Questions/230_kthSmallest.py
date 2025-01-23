# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        inorder_arr = []
        def inorder(node):

            if node == None:
                return
            
            inorder(node.left)
            inorder_arr.append(node.val)
            inorder(node.right)

        inorder(root)
        return inorder_arr[k-1]
    
sol = Solution()
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

print(sol.kthSmallest(root, 1)) # expected: 1
        