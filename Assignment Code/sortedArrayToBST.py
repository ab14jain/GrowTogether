#https://www.scaler.com/academy/mentee-dashboard/class/325338/assignment/problems/226?navref=cl_tt_nv

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        n = len(A)
        def createBST(arr, s, e):          

            if s > e:
                return None
            else:
                mid = (s+e)//2
                
                root = TreeNode(arr[mid])
                root.left = createBST(arr, s, mid-1)
                root.right = createBST(arr, mid+1, e)
                
                return root
        
        return createBST(A, 0, n-1)
    

s=Solution()
root = s.sortedArrayToBST([1, 2, 3, 4, 5])
root = s.sortedArrayToBST([1, 2, 3, 5, 10])

def inorder(node):
    if node == None:
        return

    inorder(node.left)
    print(node.val)
    inorder(node.right)

inorder(root) # 1 2 3 4 5
            
            