#https://www.scaler.com/academy/mentee-dashboard/class/325326/homework/problems/31?navref=cl_tt_nv

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def swapPairs(self, A):
			
            if A == None or A.next == None:
                return A
            
            slow = A
            fast = A.next

            swapped_ll = ListNode(-1)
            swapped_pointer = swapped_ll
            while fast:				
                after_pair = fast.next   
                slow.next = after_pair

                swapped_pointer.next = fast
                swapped_pointer = swapped_pointer.next
                swapped_pointer.next = slow
                swapped_pointer = swapped_pointer.next                
				
                slow = slow.next
                if slow:
                    fast = slow.next
                else: 
                    fast = None
                

            return swapped_ll.next



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)

s=Solution()
hd=s.swapPairs(head)

while hd: 
    print(hd.val)
    hd = hd.next
