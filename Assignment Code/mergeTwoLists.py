#https://www.scaler.com/academy/mentee-dashboard/class/325326/assignment/problems/36?navref=cl_tt_nv

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):

            curr1 = A
            curr2 = B
            merged_head = ListNode(-1)
            curr = merged_head
            while curr1 and curr2:
				
                if curr1.val < curr2.val:
                    curr.next = curr1
                    curr = curr.next
                    curr1 = curr1.next
                else:
                    curr.next = curr2
                    curr = curr.next
                    curr2 = curr2.next
				
            if curr1:
                curr.next = curr1
            
            if curr2:
                curr.next = curr2

            return merged_head.next
     
    
s=Solution()

head1 = ListNode(5)
# head1.next = ListNode(8)
# head1.next.next = ListNode(20)

head2 = ListNode(4)
# head2.next = ListNode(11)
# head2.next.next = ListNode(15)

print(s.mergeTwoLists(head1,head2))