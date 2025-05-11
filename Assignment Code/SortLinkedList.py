#https://www.scaler.com/academy/mentee-dashboard/class/325326/assignment/problems/34?navref=cl_tt_nv

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def sortList(self, A):
            
            def get_middle(head):
                slow = head
                fast = head

                while (fast and fast.next and fast.next.next):
                    fast = fast.next.next
                    slow = slow.next
                return slow

            def mergeTwoLists(A, B):

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
            

            def merge_sort(head):                
                
                if not head or head.next == None:
                    return head
                 
                leftA = get_middle(head)
                rightA = leftA.next
                leftA.next = None

                left_sort = merge_sort(head) 
                right_sort = merge_sort(rightA) 
                return mergeTwoLists(left_sort, right_sort)

            return merge_sort(A)


s=Solution()
head = ListNode(3)
head.next = ListNode(4)
head.next.next = ListNode(2)
head.next.next.next = ListNode(8)
head.next.next.next.next = ListNode(1)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(7)
hd = s.sortList(s.sortList(head))

while hd: 
    print(hd.val)
    hd = hd.next