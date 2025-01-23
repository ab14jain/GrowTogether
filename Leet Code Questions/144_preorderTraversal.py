# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        # ans = []
        # def traversePreorder(node):
        #     if node == None:
        #         return           

        #     ans.append(node.val)
        #     traversePreorder(node.left)            
        #     traversePreorder(node.right)
        
        # traversePreorder(root)
    
        # return ans

        # Approach 2 - Iterative
        stack = []
        curr = root
        ans = []
        while curr != None or stack:  

            if curr != None:
                ans.append(curr.val)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()                
                curr = curr.right
        
        return ans
    
s=Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(s.preorderTraversal(root)) #[1,2,3]