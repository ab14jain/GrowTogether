# Definition for singly-linked list.
import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:


        def reverseKNode(node, start, end):
            
            if not node or start == end:
                return node
            
            start_prev = None
            last_node = None

            curr = node
            count = 0
            while curr and count < start:
                start_prev = curr
                curr = curr.next
                count += 1

            while curr and count < end:
                curr = curr.next
                last_node = curr
                count += 1
            
            
            if start_prev:
                curr = start_prev.next
                prev = last_node if last_node else None
            else:
                curr = node
                prev = last_node if last_node else None
            
            times = k

            while curr and times > 0:

                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

                times -= 1

            if start_prev:
                start_prev.next = prev  
            else:
                node = prev  
        
            return node
        
        total_node = 0
        curr = head

        while curr:
            total_node += 1
            curr = curr.next

        times = total_node // k
        start_idx = 0
        end_idx = start_idx + k
        while times:
            head = reverseKNode(head, start_idx , end_idx)
            start_idx += k
            end_idx = start_idx + k
            times -= 1

        return head
    
s=Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)

hd = s.reverseKGroup(head, 3)

while hd:
    print(hd.val, end=" ")
    hd = hd.next