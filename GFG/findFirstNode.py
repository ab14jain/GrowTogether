#https://www.geeksforgeeks.org/problems/find-the-first-node-of-loop-in-linked-list--170645/1

""" Node Class
    class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
"""
class Solution:
    def findFirstNode(self, head):
        #code here
        
        fast = head
        slow = head

        while slow and fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
            
            if slow == fast:                
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow
            
        return None