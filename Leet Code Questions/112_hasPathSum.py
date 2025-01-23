# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        if root.left == None and root.right == None:
            return targetSum == root.val
        
        remaining_sum = targetSum - root.val
        return self.hasPathSum(root.left, remaining_sum) or self.hasPathSum(root.right, remaining_sum)