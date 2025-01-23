#https://www.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1
# Link list Node
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None
        
class Solution:
    def cloneLinkedList(self, head):
        # code here