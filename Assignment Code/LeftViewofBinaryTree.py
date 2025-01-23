#https://www.scaler.com/academy/mentee-dashboard/class/325332/assignment/problems/4675?navref=cl_tt_nv

# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):

        queue = []
        curr = A
        queue.append(curr)
        result = []
        while queue:
            size = len(queue)         

            for count in range(size):
                curr = queue.pop(0)
                if count == 0:
                    result.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)               
            
        return result
    

# Time complexity: O(n)
# Space complexity: O(n) where n is the number of nodes in the tree
s=Solution()
root = TreeNode(26)
root.left = TreeNode(10)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.right.right = TreeNode(4)

print(s.solve(root)) # [[26], [10, 3], [4, 6, 4]]