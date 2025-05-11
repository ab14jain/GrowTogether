# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head
        prev = None
        while fast and fast.next:

            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = slow.next

        return head
    
head = ListNode(1)
# head.next = ListNode(3)
# head.next.next = ListNode(4)
# head.next.next.next = ListNode(7)
# head.next.next.next.next = ListNode(1)
# head.next.next.next.next.next = ListNode(2)
# head.next.next.next.next.next.next = ListNode(6)
s=Solution()
ne_h = s.deleteMiddle(head)

while ne_h:
    print(ne_h.val, end="->")
    ne_h = ne_h.next