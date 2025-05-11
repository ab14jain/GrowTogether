#https://www.scaler.com/academy/mentee-dashboard/class/325322/assignment/problems/331?navref=cl_tt_lst_nm

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
	def lPalin(self, A):
		
            slow = A
            fast = A
			
            while fast and fast.next and fast.next.next:				
                slow = slow.next
                fast = fast.next.next
				
            second_half = slow.next
            slow.next = None
            first_half = A
			
            sh = second_half
            prev = None
            while sh:
				
                temp = sh.next
                sh.next = prev
                prev = sh
                sh = temp

            
            p1 = first_half
            p2 = prev

            while p1 and p2:
                  
                if p1.val != p2.val:
                    return 0

                p1 = p1.next
                p2 = p2.next
                
            return 1


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

s=Solution()
print(s.lPalin(head))