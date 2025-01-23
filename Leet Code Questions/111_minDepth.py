# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def get_height(node):
            if node == None:
                return -1

            return 1 + self.minDepth(node.left) + self.minDepth(node.right)
        
        if root == None:
            return 0
        
        lh = get_height(root.left)
        rh = get_height(root.right)
        min_depth = min(lh, rh)

        return min_depth + 1
        