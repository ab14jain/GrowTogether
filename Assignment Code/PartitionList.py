# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def partition(self, A, B):
		

            # lesser_than_B = {}
            # curr = A
            # prev = None
            # while curr:				
            #     if curr.val == B:
            #         while curr:
            #             next = None
            #             if curr.val < B:
            #                 next = curr.next
            #                 prev.next = next
            #                 temp = curr                            
            #                 temp.next = None
                            
            #                 if curr.val in lesser_than_B:                                
            #                     lesser_than_B[curr.val].append(temp)
            #                 else:
            #                     lesser_than_B[curr.val] = [temp]

                            
            #             prev = curr 
            #             if next: 
            #                 curr = next
            #             else:
            #                 curr = curr.next
            
            #     if curr:
            #         curr = curr.next
            #     else:
            #         break
			
            dummy1 = ListNode(-1)
            less_B = dummy1
			
            dummy2 = ListNode(-1)
            greater_B = dummy2
			
            curr = A
			
            while curr:
				
                if curr.val < B:
                    less_B.next = ListNode(curr.val)
                    less_B = less_B.next
                else:
                    greater_B.next = ListNode(curr.val)
                    greater_B = greater_B.next

                curr = curr.next

            less_B.next = dummy2.next
            return dummy1.next

            


head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)

s=Solution()
print(s.partition(head, 3))
				

