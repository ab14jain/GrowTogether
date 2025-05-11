class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here

        max_sum = float('-inf')
        def find_sum(node):

            if node == None:
                return 0
            
            left = max(0, find_sum(node.left))
            right = max(0, find_sum(node.right))
            
            
            
            nonlocal max_sum
            max_sum = max(max_sum, node.data+left+right)


            return node.data + max(left,right)

        
        find_sum(root)

        return max_sum
    
root = Node(10)
root.left = Node(2)
root.right = Node(10)

root.left.left = Node(20)
root.right.right = Node(1)

root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)

s=Solution()

print(s.findMaxSum(root))