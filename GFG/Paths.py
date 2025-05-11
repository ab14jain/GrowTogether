#https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1

from typing import Optional
from collections import deque

from typing import List



#definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def Paths(self, root):
        # code here
        ans = []
        def recur_path(node, currPath):

            if node == None:
                return

            currPath.append(node.data)

            if node.left == None and node.right == None:                
                ans.append(list(currPath))
            else:   
                recur_path(node.left, currPath)
                recur_path(node.right, currPath)
            
            currPath.pop()


        recur_path(root, [])

        return ans
    

s = Solution()
root = Node()
root.data = 1
root.left = Node()
root.left.data = 2
root.right = Node()
root.right.data = 3
root.right.left = None
root.right.right = None
root.left.left = Node()
root.left.left.data = 4
root.left.left.left = None
root.left.left.right = None
root.left.right = Node()
root.left.right.data = 5
root.left.right.left = None
root.left.right.right = None

print(s.Paths(root))
        