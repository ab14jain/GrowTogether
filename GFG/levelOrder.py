#https://www.geeksforgeeks.org/problems/level-order-traversal/1

from collections import deque

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Solution:
    def levelOrder(self, root):
        # Your code here
        if root == None:
            return []
        
        q = deque()        
        q.append(root)
        res = []
        while q:
            size = len(q)
            nodes = []
            while size:
                curr = q.popleft()
                nodes.append(curr.data)
                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
                size -= 1
            
            res.append(nodes)

        return res
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)

s=Solution()
print(s.levelOrder(None))