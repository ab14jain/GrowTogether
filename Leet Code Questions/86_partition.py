# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        dummy1 = ListNode(-1)
        head1 = dummy1

        dummy2 = ListNode(-1)
        head2 = dummy2

        curr = head

        while curr:

            if curr.val < x:
                head1.next = ListNode(curr.val)
                head1 = head1.next
            else:
                head2.next = ListNode(curr.val)
                head2 = head2.next
            curr = curr.next

        head1.next = dummy2.next

        return dummy1.next
        