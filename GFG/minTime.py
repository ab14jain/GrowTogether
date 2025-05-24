# https://www.geeksforgeeks.org/problems/burning-tree/1

from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def minTime(self, root, target):
        # code here

        # Approach 1 -> is BFS
        # parents = {
        #     root: None
        # }

        # q = deque()
        # q.append(root)

        # src = None

        # while q:
        #     curr = q.popleft()
            
        #     if curr.data == target:
        #         src = curr

        #     if curr.left:
        #         parents[curr.left] = curr
        #         q.append(curr.left)
            
        #     if curr.right:
        #         parents[curr.right] = curr
        #         q.append(curr.right)



        # q2 = deque()
        # q2.append(src)
        # time = -1
        # visited = set()
        # while q2:
        #     size = len(q2)            
        #     while size:
        #         curr = q2.popleft()
        #         visited.add(curr)

        #         if curr.left and curr.left not in visited:
        #             q2.append(curr.left)

        #         if curr.right and curr.right not in visited:
        #             q2.append(curr.right)
                
        #         if parents[curr] and parents[curr] not in visited:
        #             q2.append(parents[curr])                   
                    

        #         size -= 1       
            
        #     time += 1

        # return time

        # Approach 2 -> max len from src node to leaf node using recursion

        src = None

        def find_target(node, target):

            if node == None:
                return
            
            if node.data == target:
                src = node
                return
            
            if node.left:
                find_target(node.left, target)
            
            if node.right:
                find_target(node.left, target)

        depth = 0
        def find_depth(node):

            if node == None:
                return 0
            
            
            return 1 + max(find_depth(node.left), find_depth(node.right))
        
    
        if root == None:
            return -1
        
        if root.data == target:
            d = find_depth(root) - 1
            depth = max(depth, d)
            return

        return depth
            





s=Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)
print(s.minTime(root, 2))
        
                