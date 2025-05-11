#https://www.scaler.com/academy/mentee-dashboard/class/325326/assignment/problems/4226?navref=cl_tt_nv
# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):

        slow = A
        fast = A

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                slow = A
                prev = None
                
                while slow != fast:
                    slow = slow.next
                    prev = fast
                    fast = fast.next
                
                prev.next = None
        
        return A
