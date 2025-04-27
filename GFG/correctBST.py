#https://www.geeksforgeeks.org/problems/fixed-two-nodes-of-a-bst/1
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:  

    
    def correctBST(root):        
        def correctBSTUtil(root, first, middle, last, prev):
            if root is None:
                return
            
            correctBSTUtil(root.left, first, middle, last, prev)
        
            if prev[0] and root.data < prev[0].data:           
                if not first[0]:
                    first[0] = prev[0]
                    middle[0] = root            
                else:
                    last[0] = root
            
            prev[0] = root
            correctBSTUtil(root.right, first, middle, last, prev)
           

        first, middle, last, prev = [None], [None], [None], [None]        
        correctBSTUtil(root, first, middle, last, prev)        
        if first[0] and last[0]:
            first[0].data, last[0].data = last[0].data, first[0].data
        elif first[0] and middle[0]:
            first[0].data, middle[0].data = middle[0].data, first[0].data