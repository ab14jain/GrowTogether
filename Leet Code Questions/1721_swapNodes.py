# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        node_count = 0
        curr = head

        while curr:
            node_count += 1
            curr = curr.next
        
        counter = 1
        first_node = None
        last_node = None
        curr = head
        while counter <= node_count:

            if counter == k:
                first_node = curr
            
            if counter == (node_count - k + 1):
                last_node = curr              

            curr = curr.next
            counter += 1
        
        temp = last_node.val
        last_node.val = first_node.val
        first_node.val = temp
        return head
    
s=Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

head = s.swapNodes(head,5)

while head:
    print(head.val, end=" ")
    head = head.next