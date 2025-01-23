# https://www.scaler.com/academy/mentee-dashboard/class/325338/assignment/problems/221?navref=cl_tt_nv
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

import sys
sys.setrecursionlimit = 10**6

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isValidBST(self, A):
            curr = A
            prev = -float('inf')
            ans = 1
            def inorder(node):                
                if node == None:
                    return                 

                inorder(node.left)
                nonlocal ans, prev
                if node.val <= prev:
                    ans = 0
                prev = node.val
                inorder(node.right)               

            inorder(curr)

            return ans
     

root = TreeNode(4)
root.right = TreeNode(5)
root.right.left = TreeNode(3)

s=Solution()
print(s.isValidBST(root)) # 0