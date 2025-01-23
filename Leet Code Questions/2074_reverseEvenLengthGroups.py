# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseKNode(node, start, end, node_count):
            
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
            
            times = node_count

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

        if total_node < 2:
            return head
        
        start_idx = 1
        end_idx = 2

        factor = 0
        while start_idx < total_node:
            head = reverseKNode(head, start_idx , end_idx)
            start_idx += k
            end_idx = start_idx + k
            times -= 1

        return head
        