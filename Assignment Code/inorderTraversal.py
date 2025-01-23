# https://www.scaler.com/academy/mentee-dashboard/class/325336/assignment/problems/214?navref=cl_tt_lst_nm
# Definition for a  binary tree node

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, A):

            ans = []
            def printInorder(root):
                if root == None or root == -1:
                    return

                self.inorderTraversal(root.left)
                ans.append(root.val)
                self.inorderTraversal(root.right)
            
            printInorder(A)

            return ans

# Time complexity: O(n)
# Space complexity: O(H) where H is the height of the tree

s=Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(s.inorderTraversal(root)) # 1 3 2
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print(s.inorderTraversal(root)) # 1 3 2 4 5 6