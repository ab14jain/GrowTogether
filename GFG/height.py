#https://www.geeksforgeeks.org/problems/height-of-binary-tree/1

# Node Class:
from collections import deque


class TNode:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here

        # Recursion

        # def get_height(node):

        #     if node == None:
        #         return -1
            
        #     left_height = get_height(node.left)
        #     right_height = get_height(node.right)

        #     return max(left_height, right_height) + 1
        
        # return get_height(root)

        # Iteration
        q = deque()

        if root == None:
            return 0

        q.append(root)
        height = 0
        while q:
            size = len(q)

            while size:
                curr = q.popleft()
                
                if curr.left:
                    q.append(curr.left)

                if curr.right: 
                    q.append(curr.right)

                size -= 1

            height += 1

        return height


    
s=Solution()

rc = TNode(12)
rc.data = 12
rc.left = TNode()
rc.left.data = 12
rc.right = TNode()
rc.right.data = 12
rc.left.left = TNode()
rc.left.left.data = 5
rc.left.right = TNode()
rc.left.right.data = 22

print(s.height(rc))

