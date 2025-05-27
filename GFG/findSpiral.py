#https://www.geeksforgeeks.org/problems/level-order-traversal-in-spiral-form/1
from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None  

class Solution:
    def findSpiral(self, root):
        #code here

        # ans = []

        # def recur_path(node, left_to_right):

        #     if node == None:
        #         return               
            
        #     if not left_to_right:
        #         if node.left:
        #             ans.append(node.left.data)
                
        #         if node.right:
        #             ans.append(node.right.data)
        #     else:
        #         if node.right:
        #             ans.append(node.right.data)

        #         if node.left:
        #             ans.append(node.left.data)
            
        #     if left_to_right:
        #         if node.left:
        #             recur_path(node.left, not left_to_right)
        #         if node.right:
        #             recur_path(node.right, not left_to_right)
        #     else:
        #         if node.right:
        #             recur_path(node.right, not left_to_right)
        #         if node.left:
        #             recur_path(node.left, not left_to_right)
                
        # ans.append(root.data)
        # recur_path(root, True)
        # return ans

        
        ans = []
        q = deque()        
        q.append(root)
        left_to_right = True
        while q:      
            size = len(q)

            while size:      

                if left_to_right:
                    curr = q.pop()           
                    ans.append(curr.data)
                    if curr.right:
                        q.appendleft(curr.right)

                    if curr.left:
                        q.appendleft(curr.left)                      
                else:
                    curr = q.popleft()           
                    ans.append(curr.data)
                    if curr.left:
                        q.append(curr.left)
                    
                    if curr.right:
                        q.append(curr.right)
                
                size -= 1

            left_to_right = not left_to_right
        
        return ans


s=Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)

print(s.findSpiral(root))