#https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        # ans = []
        # def traversePostorder(node):
        #     if node == None:
        #         return           
            
        #     traversePostorder(node.left)            
        #     traversePostorder(node.right)
        #     ans.append(node.val)
        
        # traversePostorder(root)
    
        # return ans

        # Approach 2 - Iterative
        stack = []
        curr = root
        ans = []
        while curr != None or stack:  

            if curr != None:                
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()      
                curr = curr.right
                ans.append(curr.val)
        
        return ans