#https://www.scaler.com/academy/mentee-dashboard/class/325320/homework/problems/231?navref=cl_tt_nv

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : root node of tree
	# @return an integer
	def isSameTree(self, A, B):

            def comp_bst(root1, root2):
                
                if root1 == None and root2 == None :
                    return 1
                     
                if (root1 == None and root2) or (root2 == None and root1):
                    return 0
                
                if root1.val != root2.val:
                    return 0
                
                if (root1.val == root2.val and comp_bst(root1.left, root2.left) 
                    and comp_bst(root1.right, root2.right)):
                    return 1
                else:
                    return 0
                
            return comp_bst(A, B)
                