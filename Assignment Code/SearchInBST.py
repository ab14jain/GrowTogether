# https://www.scaler.com/academy/mentee-dashboard/class/325338/assignment/problems/35476?navref=cl_tt_lst_nm
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        curr = A
        while curr:

            if curr.val == B:
                return 1
            elif curr.val < B:
                curr = curr.right
            else:
                curr = curr.left

        return 0
    
