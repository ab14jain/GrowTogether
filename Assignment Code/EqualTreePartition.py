# https://www.scaler.com/academy/mentee-dashboard/class/325336/assignment/problems/4859?navref=cl_tt_nv
import sys
setmax = sys.setrecursionlimit(10**6)
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

        desired_sum = float('inf')        
        ans = 0
        def find_sum(root):
            if root == None:
                return 0            

            sub_tree_sum = find_sum(root.left) + find_sum(root.right) + root.val

            nonlocal ans
            if sub_tree_sum == desired_sum:
                ans = 1
            
            return sub_tree_sum


        total_sum = find_sum(A)
        if total_sum % 2 != 0:
            return 0
        
        desired_sum = total_sum // 2

        find_sum(A)
        return ans
    
# Time complexity: O(n)
# Space complexity: O(H) where H is the height of the tree

s=Solution()
root = TreeNode(900)
# root.left = TreeNode(None)
root.right = TreeNode(218)
root.right.right = TreeNode(682)


print(s.solve(root)) # 0


            