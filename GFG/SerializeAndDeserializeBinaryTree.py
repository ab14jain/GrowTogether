class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serializePreOrder(self, root, arr):
        if root is None:
            arr.append(-1)
            return
        
        arr.append(root.data)        
        
        self.serializePreOrder(root.left, arr)
        self.serializePreOrder(root.right, arr)
    
    def serialize(self, root):
        arr = []
        self.serializePreOrder(root, arr)
        return arr
    
    #Function to deserialize a list and construct the tree.   
    def deserializePreOrder(self, i, arr):  
        if arr[i[0]] == -1:
            i[0] += 1
            return None
        root = Node(arr[i[0]])
        i[0] += 1        
        
        root.left = self.deserializePreOrder(i, arr)
        root.right = self.deserializePreOrder(i, arr)
        
        return root

    
    def deSerialize(self, arr):
        i = [0]
        return self.deserializePreOrder(i, arr)