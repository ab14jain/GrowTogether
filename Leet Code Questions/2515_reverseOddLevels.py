# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        q = deque([root])
        level = 0

        while q:
            n = len(q)
            lvl_nodes = []

            for i in range(n):
                curr = q.popleft()
                lvl_nodes.append(curr)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            if level % 2 == 1:
                n = len(lvl_nodes)
                for j in range(n // 2):
                    lvl_nodes[j].val, lvl_nodes[n - j - 1].val = lvl_nodes[n - j - 1].val, lvl_nodes[j].val

            level += 1

        return root
    
    def printTree(self, root: Optional[TreeNode]) -> None:
        q = deque([root])

        while q:
            size = len(q)

            for _ in range(size):
                curr = q.popleft()
                print(curr.val, end=" ")

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        print()


s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s.printTree(s.reverseOddLevels(root)) # 1 3 2 5 4

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

s.printTree(s.reverseOddLevels(root)) # 1 3 2 6 5 4

            