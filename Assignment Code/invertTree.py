#https://www.scaler.com/academy/mentee-dashboard/class/325320/homework/problems/334?navref=cl_tt_nv

# Definition for a  binary tree node
from collections import deque


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return the root node in the tree
	def invertTree(self, A):		
            q = deque()
            q.append(A)
			
            while q:				
                curr = q.pop()
				
                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

                curr.left, curr.right = curr.right, curr.left

            return A
      
s=Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(s.invertTree(root))
