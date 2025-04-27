#https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def LCA(self, root, n1, n2):
        # your code here

        # def lca(node, n1, n2):
        #     if node == None:
        #         return None
            
        #     if node.data == n1 or node.data == n2:
        #         return node
            
        #     ll = lca(node.left, n1, n2)
        #     rr = lca(node.right, n1, n2)

        #     if ll != None and rr != None:
        #         return node

        #     if ll != None:
        #         return ll
            
        #     if rr != None:
        #         return rr
            
        #     return None
    
        # return lca(root, n1, n2)

        while root:   
            if root.data > n1.data and root.data > n2.data:
                root = root.left  
            elif root.data < n1.data and root.data < n2.data:
                root = root.right            
            else:
                break
                
        return root