# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> Optional[TreeNode]:
        

        def create_bst(arr, s , e):

            if s > e:
                return None
            
            root = TreeNode(arr[s])

            i = s+1
            left_arr = []
            right_arr = []
            while i <= e and arr[i] < root.val:
                # left_arr.append(arr[i])
                i += 1            
            right_arr = arr[i:e+1]

            # root.left = create_bst(left_arr, s+1, i-1)
            # root.right = create_bst(right_arr, i, e)

            left_arr = arr[s+1:i]
            right_arr = arr[i:e+1]
            root.left = create_bst(arr, s+1, i-1)
            root.right = create_bst(arr, i, e)

            return root
        
        return create_bst(preorder, 0, len(preorder)-1)
    
sol = Solution()
# root = (sol.bstFromPreorder([8,5,1,7,10,12])) # expected: 8
root = (sol.bstFromPreorder([4,2])) # expected: 8

# Time complexity: O(n)
# Space complexity: O(n)

# The above solution can be optimized by using a stack to keep track of the nodes.
   

def preorder_traversal(preorder):

    if preorder == None:
        return
    print(preorder.val)
    preorder_traversal(preorder.left)    
    preorder_traversal(preorder.right)   

preorder_traversal(root) # expected: 8 5 1 7 10 12