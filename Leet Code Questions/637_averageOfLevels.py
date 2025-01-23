# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        queue = []
        result = []
        curr = root

        queue.append(curr)

        while queue:

            size = len(queue)
            t_sum = 0            
            for s in range(size):
                node = queue.pop(0)
                t_sum += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            result.append(t_sum/size)

        return result
    
# Time complexity: O(n)
# Space complexity: O(H)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


s=Solution()
print(s.averageOfLevels(root)) # [3.0, 14.5, 11.0]
