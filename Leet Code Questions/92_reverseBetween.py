# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        curr = head
        start_prev = None
        last = None

        if not head or left == right:
            return head

        count = 1
        while curr and count < left:
            start_prev = curr
            curr = curr.next
            count += 1

        count = 0
        curr = head
        while curr and count < right:            
            curr = curr.next
            last = curr
            count += 1   
        

        if start_prev:
            prev = last if last else None
            curr = start_prev.next
        else:
            prev = last if last else None
            curr =  head

        times = (right - left + 1)
        while curr and times > 0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            times -= 1

        if start_prev:
            start_prev.next = prev  
        else:
            head = prev     


        return head



s=Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
def printlist(head):
    while head:
        print(head.val, end = " ")
        head = head.next

# hd = s.reverseBetween(head, 2, 4)
# printlist(hd)
# hd = s.reverseBetween(head, 1, 3)
# printlist(hd)
# print()
# hd = s.reverseBetween(head, 1, 4)
# printlist(hd)
# print()
hd = s.reverseBetween(head, 2,3)
printlist(hd)
print()

