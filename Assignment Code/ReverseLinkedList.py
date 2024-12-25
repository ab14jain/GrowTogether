#https://www.scaler.com/academy/mentee-dashboard/class/325316/assignment/problems/40?navref=cl_tt_lst_nm
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reverseList(self, A):

            prev = None
            temp = A

            while temp:
                nxt = temp.next
                temp.next = prev
                prev = temp
                temp = nxt
            A = prev
            return A
	

# create a linked list

# 1->2->3->4->5->6->7->8->9->10
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# create a solution object
sol = Solution()

# reverse the linked list
head = sol.reverseList(head)

# print the reversed linked list
while head:
    print(head.val, end=" ")
    head = head.next

