# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        
        curr = A
        res = []
        while curr:

            if curr.left == None:
                res.append(curr.val)
                curr = curr.right
            else:
                temp = curr.left

                while temp.right != None and temp.right != curr:
                    temp = temp.right

                if temp.right == None:
                    temp.right = curr
                    curr = curr.left
                else:
                    res.append(curr.data)
                    curr = curr.right
