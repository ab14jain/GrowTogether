# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = []
        result = []
        curr = root

        if curr == None:
            return []
        
        queue.append(curr)

        while queue:
            size = len(queue)
            temp = []
            for s in range(size):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            result.append(temp)

        result.reverse()
        return result

        