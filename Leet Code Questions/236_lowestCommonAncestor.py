# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lca(root):

            if root == None:
                return None
            
            if (root == p or root == q):
                return root

            left = lca(root.left)            
            right = lca(root.right)

            if left and right:
                return root
            
            if not left:
                return left            
           
            return right

        return lca(root)
