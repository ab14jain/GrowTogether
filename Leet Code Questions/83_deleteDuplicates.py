# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ans = head
        
        while head and head.next:

            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        
        return ans   
        
    

s = Solution()

# 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)

head = s.deleteDuplicates(head)
while head:
    print(head.val)
    head = head.next
