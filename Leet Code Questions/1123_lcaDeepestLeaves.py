# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        depth_mp = {}
        max_depth = float('-inf')

        def populate_depth(node:TreeNode, depth):

            if not node:
                return 
            
            depth_mp[node.val] = depth
            nonlocal max_depth
            max_depth = max(max_depth, depth)

            if node.left:
                populate_depth(node.left, depth+1)
            
            if node.right:
                populate_depth(node.right, depth+1)

        def lca(root):

            if root == None or depth_mp[root.val] == max_depth:
                return root
            

            left = lca(root.left)
            right = lca(root.right)

            if left and right:
                return root
            
            if left:
                return left
            
            return right
        
        populate_depth(root, 0)
        return lca(root)
        


s=Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)

root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

print(s.lcaDeepestLeaves(root).val)