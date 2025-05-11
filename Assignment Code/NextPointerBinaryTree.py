# Definition for a  binary tree node
from collections import deque


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):

        if root == None:
            return None

        q = deque()
        q.append(root)


        while q:
            size = len(q)
            n = len(q)
            i = 0
            tempq = list(q)
            while size > 0:
                curr = q.popleft()
                if tempq and i < n-1:
                    curr.next = tempq[i+1]
                
                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
                size -= 1
                i += 1
            
            

        return root


root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.right = TreeLinkNode(5)
root.left.left = TreeLinkNode(3)
root.left.right = TreeLinkNode(4)
root.right.left = TreeLinkNode(6)
root.right.right = TreeLinkNode(7)

s=Solution()
rt= s.connect(None)
        