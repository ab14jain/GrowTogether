# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
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

       

s=Solution()

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(4)
head.next.next.next = head.next

hd = s.detectCycle(head)