# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        n = len(preorder)        
        def createTree(inorder, preorder, in_s, in_e, ps_s, ps_e):				
            if in_s > in_e or ps_s > ps_e:
                return None
            
            root = TreeNode(preorder[ps_s])
            root_idx = inorder.index(preorder[ps_s])

            x = root_idx - in_s + ps_s

            root.left = createTree(inorder, preorder, in_s, root_idx - 1, ps_s+1, x)
            root.right = createTree(inorder, preorder, root_idx + 1, in_e, x + 1, ps_e)

            return root
            
        return createTree(inorder, preorder, 0, n-1, 0, n-1)