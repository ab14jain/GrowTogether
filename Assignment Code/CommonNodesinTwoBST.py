# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def solve(self, A, B):

        set_A = set()
        set_B = set()
        MOD = 1000000007
        def inorder_traverse(root:TreeNode, res_set:set):

            if root == None:
                return
            
            inorder_traverse(root.left,res_set)
            res_set.add(root.val)
            inorder_traverse(root.right,res_set)
        

        inorder_traverse(A,set_A)
        inorder_traverse(B,set_B)

        ans =  0
        for key in set_A:
            if key in set_B:
                ans = (ans + key)%MOD      
        
        
        return ans%MOD

