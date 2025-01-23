# https://www.scaler.com/academy/mentee-dashboard/class/325332/assignment/problems/224?navref=cl_tt_lst_nm

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
            # def createTree(inorder, postorder, in_s, in_e, ps_s, ps_e):				
            #     if in_s > in_e or ps_s > ps_e:
            #         return None
                
            #     root = TreeNode(postorder[ps_e])
            #     root_idx = inorder.index(postorder[ps_e])
            #     x = root_idx + ps_s - in_s - 1
            #     root.left = createTree(inorder, postorder, in_s, root_idx - 1, ps_s, x)
            #     root.right = createTree(inorder, postorder, root_idx + 1, in_e, x + 1, ps_e-1)

            #     return root
            
            # return createTree(A, B, 0, n-1, 0, n-1)
			           
            inorder = A
            postorder = B

            if not postorder or not inorder:
                return None
            
            root_val = postorder[-1]
            root = TreeNode(root_val)
            
            root_idx = inorder.index(root_val)
			
            
            
            root.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])    
            root.right = self.buildTree(inorder[root_idx+1:], postorder[root_idx:-1])
            
            return root
      

s=Solution()
root = s.buildTree([4,2,7,5,1,3,6], [4,7,5,2,6,3,1])