# https://www.scaler.com/academy/mentee-dashboard/class/325336/homework/problems/4401?navref=cl_tt_nv

# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):

        curr = A
        if curr == None:
            return 0     

        def find_sum(root):
            if root == None:
                return 0
            
            subtree_sum = find_sum(root.left) + find_sum(root.right) + root.val

            return subtree_sum
        
        total_sum = find_sum(A.left) + find_sum(A.right)

        if total_sum == A.val:
            return 1
        
        return 0

# Time complexity: O(n)
# Space complexity: O(H) where H is the height of the tree

s=Solution()
root = TreeNode(26)
root.left = TreeNode(10)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.right.right = TreeNode(4)

print(s.solve(root)) # 1
