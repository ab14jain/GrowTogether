# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def reverseList(self, A, B):
            
            def reverseBetween(LL, sIndex, eIndex):
		
                start_prev = None
                last_next = None
                start = None            
                curr = LL              
                

                if not LL or sIndex == eIndex:
                    return LL
                
                count = 1
                while curr:
                    if count == sIndex:
                        start = curr
                        break

                    start_prev = curr
                    curr = curr.next
                    count += 1

                rev_curr = start
                rev_prev = None
                while rev_curr and count != eIndex:
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
                    LL = rev_curr
                start.next = last_next

                return LL
            
            if B == 1:
                return A
            
            count = 0
            temp = A
            while temp:
                count += 1
                temp = temp.next

            times = count//B

            i = 1
            j = B
            while times > 0:
                A = reverseBetween(A, i, j)
                i += B
                j += B
                times -= 1
            
            return A

s=Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
# head.next.next.next.next.next.next = ListNode(7)


head = s.reverseList(head, 2)

print("Reversed linked list:")
while head:
    print(head.val, end=" ")
    head = head.next