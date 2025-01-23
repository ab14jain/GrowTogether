# Definition for a binary tree node.
from typing import Optional
import sys
sys.setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, current_num):

            if node == None:
                return 0
            
            current_num = current_num*10 + node.val

            if node.left == None and node.right == None:
                return current_num

            return dfs(node.left, current_num) + dfs(node.right, current_num) 
        
        return dfs(root, 0)


        

# Time complexity: O(n)
# Space complexity: O(H)

# Example 1:

# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.

s=Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(s.sumNumbers(root)) #25
