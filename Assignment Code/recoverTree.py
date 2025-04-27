# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def recoverTree(self, A):	
            


            inorder = []
			
            def inorder_traverse(root,inorder):
				
                if root == None:
                    return
				
                inorder_traverse(root.left,inorder)
                inorder.append(root.val)
                inorder_traverse(root.right,inorder)

            inorder_traverse(A,inorder)
            print(inorder)

root =TreeNode(2)
root.left =TreeNode(3)
root.right =TreeNode(1)

s=Solution()
print(s.recoverTree(root))
				

