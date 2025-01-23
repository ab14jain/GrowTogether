#https://www.scaler.com/academy/mentee-dashboard/class/325332/homework/problems/9268?navref=cl_tt_nv

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

        result = []
        queue.append(curr)

        while queue:
            size = len(queue)       
             
            for count in range(size):
                curr = queue.pop(0)
                if curr != -1:
                    result.append(curr.val)

                    if curr.left:
                        queue.append(curr.left)
                    else:
                        queue.append(-1)

                    if curr.right:
                        queue.append(curr.right)
                    else:
                        queue.append(-1)
                else:
                    result.append(-1)
            
            
        return result



root = TreeNode(26)
root.left = TreeNode(10)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.right.right = TreeNode(4)

s=Solution()
print(s.solve(root)) # [26, 10, 3, 4, 6, 4]