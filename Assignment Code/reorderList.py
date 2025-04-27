#https://www.scaler.com/academy/mentee-dashboard/class/325326/homework/problems/33?navref=cl_tt_nv

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reorderList(self, A):
            def reverse_list(head):
                prev = None
                curr = head
                while curr:
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                
                return prev
            
            slow = A
            fast = A

            while fast and fast.next and fast.next.next:
                  
                slow = slow.next
                fast = fast.next.next

            second_half = slow.next 
            second_half = reverse_list(second_half)
            slow.next = None
            first_half = A

            curr_f = first_half
            curr_s = second_half
            

            while curr_f and curr_s:
                temp_f = curr_f.next
                temp_s = curr_s.next
                curr_s.next = temp_f
                curr_f.next = curr_s
                  
                curr_f = temp_f
                curr_s = temp_s

            return first_half
            
            
     

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
hd=s.reorderList(head)

while hd: 
    print(hd.val)
    hd = hd.next