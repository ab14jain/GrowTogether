# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:

        # Approach 1 - Recursion

        # ans = []
        # def traverseInorder(node):
        #     if node == None:
        #         return           

        #     traverseInorder(node.left)
        #     ans.append(node.val)
        #     traverseInorder(node.right)
        
        # traverseInorder(root)
    
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
                ans.append(curr.val)
                curr = curr.right
        
        return ans
    
# Time complexity: O(n)
# Space complexity: O(H)

# Example 1:

s=Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(s.inorderTraversal(root)) #[1,3,2]