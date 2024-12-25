# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        
        if root == None:
            return []

        queue = deque([(root)])
        ans = []
        while queue:            
            level = []
            level_max = float("-inf")
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                level_max = max(level_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level_max)
        
        return ans
    
# Time complexity: O(n)
# Space complexity: O(n)

# Example 1:
root = [1,3,2,5,3,None,9]
# Output: [1,3,9]
print(Solution().largestValues(root))


            