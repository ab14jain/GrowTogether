#https://www.geeksforgeeks.org/problems/find-length-of-loop/1
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #code here

        slow = head
        fast = head
        hasloop = False

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                hasloop = True
                break
        
        if not hasloop:
            return 0
            
        fast = head

        while fast and slow and fast != slow:
            fast = fast.next
            slow = slow.next
        
        count = 0
        if slow:
            nxt = slow.next
            while nxt and nxt != fast:
                nxt = nxt.next
                count += 1
    
            return count+1
        else:
            return count