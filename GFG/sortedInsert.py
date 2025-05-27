# https://www.geeksforgeeks.org/problems/sorted-insert-for-circular-linked-list/1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
   
        
class Solution:
    def sortedInsert(self, head, data):