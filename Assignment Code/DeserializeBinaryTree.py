# https://www.scaler.com/academy/mentee-dashboard/class/325332/homework/problems/9269?navref=cl_tt_nv
# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

import math
import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def solve(self, A):
        n = len(A)

        def buid_tree(A, s, e, i):
            
            if s > e or A[s] == -1:
                return None
            
            root = TreeNode(A[s])

            root.left = buid_tree(A, 2*i+1, e, 2*i+1)
            root.right = buid_tree(A, 2*i+2, e, 2*i+2)

            return root
        
        return buid_tree(A, 0, len(A)-1, 0)
    

s=Solution()
# root = s.solve([1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1])
# print(root.val)
# root = s.solve([1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1])
# print(root.val)
root = s.solve([1,2,4,-1,3,-1,5,7,-1,-1,6,-1,8,-1,-1,-1,-1])
print(root.val)
           