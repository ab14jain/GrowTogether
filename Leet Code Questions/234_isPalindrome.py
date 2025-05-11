# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def rev(node):
            
            curr = node
            prev = None
            
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                
            return prev
           
           
        reversed_list = rev(head)
        rcurr = reversed_list

        # while rcurr:            
        #     print(rcurr.val)               
        #     curr = curr.next

        curr = head
        
        while curr:            
            if curr.val != rcurr.val:
                return False
                
            curr = curr.next
            rcurr = rcurr.next
            
        return True
    

s=Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(1)

hd = s.isPalindrome(head)