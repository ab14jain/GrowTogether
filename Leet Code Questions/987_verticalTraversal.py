# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        hmap = defaultdict(list)
        q = deque()
        idx = 0
        q.append([root, (0, idx)])

        while q:
            node, (pos, idx) = q.popleft()
            hmap[idx].append((node.val, (pos, idx)))

            if node.left:
                q.append([node.left, (pos+1, idx-1)])           
            
            if node.right:
                q.append([node.right, (pos+1, idx+1)])

                
        res = []

        for i in sorted(hmap):
            temp = hmap[i]  
            temp.sort()
            temp.sort(key = lambda i: i[1])
            sorted_node = []
            for i in temp:
                sorted_node.append(i[0])

            res.append(sorted_node)
        
        return res


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(6)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(7)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(6)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.left.left = TreeNode(0)
# root.left.right = TreeNode(2)
# root.right.left = TreeNode(2)


s=Solution()
print(s.verticalTraversal(root))

