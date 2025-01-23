# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Approach 1
        # Time complexity: O(n)
        # Space complexity: O(H) where H is the height of the tree

        is_balanced = True

        def find_height(root):
            if root == None:
                return -1
            
            left_height = find_height(root.left)
            right_height = find_height(root.right)   
            
            nonlocal is_balanced
            if abs(left_height - right_height) > 1:
                is_balanced = False
            
            return 1 + max(left_height, right_height)
        
        find_height(root)            
        return is_balanced

        # Approach 2    
        # Time complexity: O(n**2)
        # Space complexity: O(H+H) where H is the height of the tree first H for isBalanced and second H for find_height

        # def find_height(root):
        #     if root == None:
        #         return -1
            
        #     left_height = find_height(root.left)
        #     right_height = find_height(root.right) 
            
        #     return 1 + max(left_height, right_height)            

        # if root == None:
        #     return True
        
        # left_height = find_height(root.left)
        # right_height = find_height(root.right)

        # if abs(left_height - right_height) > 1:
        #     return False
    
        # return self.isBalanced(root.left) and self.isBalanced(root.right)
        