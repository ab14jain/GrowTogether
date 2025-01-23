# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        curr = root
        queue.append(curr)
        result = []

        if curr == None:
            return []

        while queue:
            size = len(queue)  
            for count in range(1, size+1):
                curr = queue.pop(0)
                if count == size:
                    result.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)               
            
        return result