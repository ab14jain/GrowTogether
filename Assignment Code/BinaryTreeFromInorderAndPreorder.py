# https://www.scaler.com/academy/mentee-dashboard/class/325332/homework/problems/219?navref=cl_tt_lst_nm

import sys
sys.setrecursionlimit(10**6)

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, A, B):
		
            # n = len(A)        
            # def createTree(inorder, preorder, in_s, in_e, ps_s, ps_e):				
            #     if in_s > in_e or ps_s > ps_e:
            #         return None
                
            #     root = TreeNode(preorder[ps_s])
            #     root_idx = inorder.index(preorder[ps_s])

            #     x = root_idx - in_s + ps_s

            #     root.left = createTree(inorder, preorder, in_s, root_idx - 1, ps_s+1, x)
            #     root.right = createTree(inorder, preorder, root_idx + 1, in_e, x + 1, ps_e)

            #     return root
            
            # return createTree(B, A, 0, n-1, 0, n-1)
			
            preorder = A
            inorder = B
            if not preorder or not inorder:
                return None

            # The first element in preorder is the root
            root_value = preorder[0]
            root = TreeNode(root_value)

            # Find the root in the inorder traversal
            root_index = inorder.index(root_value)

            # Recursively build the left and right subtrees
            root.left = self.buildTree(preorder[1:1 + root_index], inorder[:root_index])
            root.right = self.buildTree(preorder[1 + root_index:], inorder[root_index + 1:])

            return root