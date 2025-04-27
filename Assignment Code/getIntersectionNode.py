
#Definition for singly-linked list
class ListNode:
   def __init__(self, val):
      self.val = val
      self.next = None

class Solution:
    def getIntersectionNode(self, A, B):
        

        
        ptr1 = A
        ptr2 = B

        
        if not ptr1 or not ptr2:
            return None

        
        while ptr1 != ptr2:
        
            ptr1 = ptr1.next if ptr1 else B
            ptr2 = ptr2.next if ptr2 else A

        
        return ptr1
        
        # head1 = A
        # head2 = B

        # while head1 and head2:

        #     if head1 == head2:
        #         return head1
            
        #     if head1.next == None:
        #         head1 = B
            
        #     if head2.next == None:
        #         head2 = A

        #     head1 = head1.next
        #     head2 = head2.next  

        # return None 
        

llA = ListNode(1)
llA.next = ListNode(2)
llA.next.next = ListNode(3)
llA.next.next.next = ListNode(4)
llA.next.next.next.next = ListNode(5)

llB = ListNode(7)
llB.next = ListNode(8)
llB.next.next = ListNode(10)
llB.next.next.next = ListNode(9)
llB.next.next.next.next = llA.next.next.next

s=Solution()

hd = s.getIntersectionNode(None, None)