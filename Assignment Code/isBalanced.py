# https://www.scaler.com/academy/mentee-dashboard/class/325332/assignment/problems/225?navref=cl_tt_nv

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isBalanced(self, A):	
            
            # Approach 1
            # Time complexity: O(n)
            # Space complexity: O(H) where H is the height of the tree
            
            # is_balanced = 1

            # def find_height(root):
            #     if root == None:
            #         return -1
                
            #     left_height = find_height(root.left)
            #     right_height = find_height(root.right)   
                
            #     nonlocal is_balanced
            #     if abs(left_height - right_height) > 1:
            #         is_balanced = 0
                
            #     return 1 + max(left_height, right_height)
            
            # find_height(A)            
            # return is_balanced


            # Approach 2    
            # Time complexity: O(n**2)
            # Space complexity: O(H+H) where H is the height of the tree first H for isBalanced and second H for find_height
			
            def find_height(root):
                if root == None:
                    return -1
                
                left_height = find_height(root.left)
                right_height = find_height(root.right) 
                
                return 1 + max(left_height, right_height)            

            if A == None:
                return 1
            
            left_height = find_height(A.left)
            right_height = find_height(A.right)

            if abs(left_height - right_height) > 1:
                return 0
        
            return self.isBalanced(A.left) and self.isBalanced(A.right)
      
# Time complexity: O(n)
# Space complexity: O(H) where H is the height of the tree

s=Solution()
root = TreeNode(26)
root.left = TreeNode(10)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
# root.right.right = TreeNode(4)

print(s.isBalanced(root)) # 1
		