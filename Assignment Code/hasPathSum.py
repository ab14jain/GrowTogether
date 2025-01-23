# https://www.scaler.com/academy/mentee-dashboard/class/325336/assignment/problems/234/?navref=cl_pb_nv_tb
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def hasPathSum(self, A, B):            
				
            if A == None:
                return 0
            
            if A.left == None and A.right == None:
                return 1 if B == A.val else 0
            
            remaining_sum = B - A.val
            return self.hasPathSum(A.left, remaining_sum) or self.hasPathSum(A.right, remaining_sum)
            
            
            
      
# Time complexity: O(n)
# Space complexity: O(H) where H is the height of the tree

s=Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)


       
		