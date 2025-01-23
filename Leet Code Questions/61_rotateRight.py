# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        prev = None
        curr = head
        last = None

        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        if k > count:
            k = k % count

        while k > 0 and curr:
            while curr.next:
                prev = curr
                curr = curr.next

            if prev:
                last = prev.next
                last.next = head
                prev.next = None          
            
            if last:
                head = last
            k -= 1
        
        return curr

# Time complexity: O(n)
# Space complexity: O(1)

s=Solution()
# head = s.rotateRight(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))),2) # 4->5->1->2->3
head = s.rotateRight(ListNode(1,ListNode(2,ListNode(3))),2000000000) # 4->5->1->2->3
# head = s.rotateRight(ListNode(1),1) # 1

while head:
    print(head.val)
    head = head.next

            