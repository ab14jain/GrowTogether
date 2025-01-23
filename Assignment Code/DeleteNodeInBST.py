# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def solve(self, A, B):

        
        def delete_node(node, k):            
            if node is None:
                return None   

            if node.val < k:
                node.right = delete_node(node.right, k)
            elif node.val > k:
                node.left = delete_node(node.left, k)
            else:                   
                # If node doesn't has child
                if node.left is None and node.right is None:
                    return None
                # If node has a child
                elif node.left is None or node.right is None:
                    if node.left:
                        return node.left
                    else:
                        return node.right
                # If node has two children
                else:
                    # Find the inorder successor
                    # temp = node.right                        
                    # while temp.left:
                    #     temp = temp.left
                    # #swapping the values
                    # curr_val = node.val
                    # node.val = temp.val
                    # temp.val = curr_val
                    # node.right = delete_node(node.right, curr_val)
                    

                    temp = node.left                        
                    while temp.right:
                        temp = temp.right
                    #swapping the values
                    curr_val = node.val
                    node.val = temp.val
                    temp.val = curr_val
                    node.left = delete_node(node.left, curr_val)
            
            return node
            
        
        return delete_node(A, B)
    

s=Solution()
# A = TreeNode(5)
# A.left = TreeNode(3)
# A.right = TreeNode(6)
# A.left.left = TreeNode(2)
# A.left.right = TreeNode(4)
# A.right.right = TreeNode(7)
# B = 3
# root = s.solve(A, B) # 5 2 4 6 7

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)

# inorder_traversal(root) # 2 4 5 6 7   

A = TreeNode(2)
A.left = TreeNode(1)
A.right = TreeNode(3)
B = 2
root = s.solve(A, B) # 5 2 4 6 7
inorder_traversal(root)
