# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:


        max_height = float('-inf')

        def height(node):

            if node == None:
                return 0
            
            left = height(node.left)
            right = height(node.right)

            nonlocal max_height
            max_height = max(max_height, left+right)
            return max(left, right) + 1
        
        height(root)
        return max_height