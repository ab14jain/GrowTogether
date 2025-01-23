# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        prev = float('-inf')
        curr = root
        ans = True
        def inorder(node):

            if node == None:
                return
            
            inorder(node.left)
            nonlocal ans, prev
            if node.val <= prev:
                ans = False
            prev = node.val
            inorder(node.right)

        inorder(root)
        return ans
        