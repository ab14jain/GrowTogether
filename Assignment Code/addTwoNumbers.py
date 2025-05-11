#http://scaler.com/academy/mentee-dashboard/class/325326/homework/problems/38?navref=cl_tt_nv

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def addTwoNumbers(self, A, B):
		
		def reverse_list(A):
			# prev = None
			# curr = A

			# while curr:

			# 	temp = curr.next
			# 	curr.next = prev

			# 	prev = curr
			# 	curr = temp
			
			# return prev
			return A

		
		rev_A = reverse_list(A)
		rev_B = reverse_list(B)
		
		p_A = rev_A
		p_B = rev_B
		carry = 0

		sum_ll = ListNode(-1)
		p_ll = sum_ll
		while p_A and p_B:
			sum = p_A.val + p_B.val + carry
			carry = sum//10
			sum = sum%10		

			p_ll.next = ListNode(sum)
			p_ll = p_ll.next

			p_A = p_A.next
			p_B = p_B.next

		while p_A:
			sum = p_A.val + carry
			carry = sum//10
			sum = sum%10

			p_ll.next = ListNode(sum)
			p_ll = p_ll.next
			p_A = p_A.next

		while p_B:
			sum = p_B.val + carry
			carry = sum//10
			sum = sum%10

			p_ll.next = ListNode(sum)
			p_ll = p_ll.next
			p_B = p_B.next

		if carry:
			p_ll.next = ListNode(carry)
			p_ll = p_ll.next
		
		return sum_ll.next

headA = ListNode(9)
headA.next = ListNode(9)
headA.next.next = ListNode(1)

headB = ListNode(1)
# headB.next = ListNode(1)
# headB.next.next = ListNode(1)

# head.next.next.next.next.next.next = ListNode(7)
# head.next.next.next.next.next.next.next = ListNode(8)
# head.next.next.next.next.next.next.next.next = ListNode(9)

s=Solution()
hd=s.addTwoNumbers(headA,headB)

while hd: 
    print(hd.val)
    hd = hd.next

