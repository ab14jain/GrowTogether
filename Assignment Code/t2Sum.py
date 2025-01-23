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
	def t2Sum(self, A, B):

            def inorder(node):
                if node == None:
                    return []
                return inorder(node.left) + [node.val] + inorder(node.right)
            
            # def revInorder(node):
            #     if node == None:
            #         return []
            #     return revInorder(node.right) + [node.val] + revInorder(node.left)  
            
            def findPair(arr, B):
                i = 0
                j = len(arr)-1
                while i < j:
                    if arr[i] + arr[j] == B:
                        return 1
                    elif arr[i] + arr[j] < B:
                        i += 1
                    else:
                        j -= 1
                return 0
            
            arr = inorder(A)
            # revArr = revInorder(A)
            return findPair(arr, B) #or findPair(revArr, B)
     

s=Solution()
root = TreeNode(10)
root.left = TreeNode(9)
root.left.left = TreeNode(2)
root.right = TreeNode(20)

print(s.t2Sum(root, 11)) # 1
