# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val


class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here

        prev = None
        slow = head
        fast = head

        while slow and fast and fast.next:

            prev = slow
            slow = slow.next
            fast = fast.next.next


            if slow == fast:

                fast = head
                while slow != fast:

                    prev = slow
                    slow = slow.next
                    fast = fast.next  
        
                prev.next = None
        
        return head
    
s=Solution()
head = Node(1)
head.next = Node(8)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head.next

hd = s.removeLoop(head)
while hd:
    print(hd.data)
    hd = hd.next
