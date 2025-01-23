# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:

        n = len(inorder)        
        def createTree(inorder, postorder, in_s, in_e, ps_s, ps_e):				
            if in_s > in_e or ps_s > ps_e:
                return None
            
            root = TreeNode(postorder[ps_e])
            root_idx = inorder.index(postorder[ps_e])
            x = root_idx + ps_s - in_s - 1
            root.left = createTree(inorder, postorder, in_s, root_idx - 1, ps_s, x)
            root.right = createTree(inorder, postorder, root_idx + 1, in_e, x + 1, ps_e-1)

            return root
        
        return createTree(inorder, postorder, 0, n-1, 0, n-1)
        