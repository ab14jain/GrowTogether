# Definition for a binary tree node.
from typing import Optional, List 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = []
        result = []
        curr = root
        if curr == None:
            return []
        
        queue.append(curr)
        direction = 1
        while queue:
            size = len(queue)
            temp = []
            for i in range(size):
                node = queue.pop(0)         
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if direction == 1:
                result.append(temp)
                direction = 0
            else:
                result.append(temp[::-1])
                direction = 1

        return result