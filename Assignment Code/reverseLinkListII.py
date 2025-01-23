#https://www.scaler.com/academy/mentee-dashboard/class/325316/homework/problems/45?navref=cl_tt_nv

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @param C : integer
	# @return the head node in the linked list
	def reverseBetween(self, A, B, C):
		
            start_prev = None
            last_next = None
            start = None            
            curr = A

            if not A or B == C:
                return A
            
            count = 1
            while curr:
                if count == B:
                    start = curr
                    break

                start_prev = curr
                curr = curr.next
                count += 1

            rev_curr = start
            rev_prev = None
            while rev_curr and count != C:
                nxt = rev_curr.next
                rev_curr.next = rev_prev
                rev_prev = rev_curr
                rev_curr = nxt

                count += 1

            
            last_next = rev_curr.next
            rev_curr.next = rev_prev

            if start_prev:
                start_prev.next = rev_curr
            else:
                A = rev_curr
            start.next = last_next

            return A
      

s=Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)


head = s.reverseBetween(head, 1,2)

print("Reversed linked list:")
while head:
    print(head.val, end=" ")
    head = head.next


