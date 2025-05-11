# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        
        def find(node, val):

            if node == None:
                return False

            if node.val == val:
                return True

            ls = find(node.left, val)
            rs = find(node.right, val)

            return ls or rs

        def findLCA(node, B, C):
            if node == None:
                return None
            
            if node.val == B or node.val == C:
                return node.val
            
            ll = findLCA(node.left, B, C)
            rr = findLCA(node.right, B, C)

            if ll != None and rr != None:
                return node.val
            
            if ll != None:
                return ll
            
            if rr != None:
                return rr
            
            return None

        if not find(A, B) or not find(A, C):
            return -1

        return findLCA(A,B,C)
       


root = TreeNode(4)
root.left = TreeNode(8)
root.right = TreeNode(7)
root.left.left = TreeNode(13)
root.left.right = TreeNode(6)




# 4 8 7 13 6 -1 -1 -1 -1 9 10 12 -1 2 11 -1 -1 -1 -1 -1 5 1 -1 -1 3 -1 -1
# 31
# 39
s=Solution()
print(s.lca(root, 14,15))