# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional, List
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        curr = root
        queue.append(curr)
        result = []

        if curr == None:
            return []

        while queue:
            size = len(queue)
            temp = []
            while size > 0:
                curr = queue.pop(0)
                temp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                size -= 1
            
            result.append(temp)
        
        return result