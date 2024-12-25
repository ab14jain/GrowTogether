# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):

            curr = A

            # 1 -> 1 -> 1 -> 1 -> 1 -> 2 -> 3 -> 3 -> None
            # C                             C    N
            while curr:
                nxt = curr.next
                while nxt:
                    if curr.val == nxt.val:
                        nxt = nxt.next
                    else:
                        break
                
                curr.next = nxt
                curr = nxt           
            
            return A
      


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(1)
head.next.next.next = ListNode(1)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(2)
head.next.next.next.next.next = ListNode(3)
head.next.next.next.next.next.next = ListNode(3)

s=Solution()
s.deleteDuplicates(head)

while head:
    print(head.val)
    head = head.next

