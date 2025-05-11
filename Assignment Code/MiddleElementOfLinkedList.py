# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        
        slow = A
        fast = A

        while (fast and fast.next and fast.next.next):

            fast = fast.next.next
            slow = slow.next

        if fast and fast.next:
            return slow.next
        return slow
    

s=Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

print(s.solve(head))
