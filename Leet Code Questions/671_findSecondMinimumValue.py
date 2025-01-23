# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        def inorder(node):
            if node == None:
                return []

            return inorder(node.left) + [node.val] + inorder(node.right)
        
        inorder_list = inorder(root)
        inorder_list = list(set(inorder_list))
        inorder_list.sort()

        return inorder_list[1] if len(inorder_list) > 1 else -1
