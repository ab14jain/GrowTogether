# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:


        def dash_count(s, n, pos):
            start = pos[0]
            while pos[0] < n and s[pos[0]] == '-':
                pos[0] += 1
            return pos[0] - start
        
        def digit(traversal, n, pos):
            val = 0
            while pos[0] < n and traversal[pos[0]].isdigit():
                val = val * 10 + int(traversal[pos[0]])
                pos[0] += 1
            return val
        
        def build_tree(node, expected_das_count, traversal, n, pos):

            if pos[0] >= n:
                return
            
            prev_pos = pos[0]
            dash_len = dash_count(traversal, n, pos)

            if dash_len != expected_das_count:
                pos[0] = prev_pos
                return
            
            node_data = digit(traversal, n, pos)
            new_node = TreeNode(node_data)

            if not node.left:
                node.left = new_node
            else:
                node.right = new_node

            build_tree(new_node, expected_das_count + 1, traversal,n,pos)
            build_tree(new_node, expected_das_count + 1, traversal,n,pos)

        n = len(traversal)
        pos = [0]

        if n == 0:
            return None

        root = TreeNode(digit(traversal, n, pos))

        build_tree(root, 1, traversal, n, pos)
        build_tree(root, 1, traversal, n, pos)

        return root
        
