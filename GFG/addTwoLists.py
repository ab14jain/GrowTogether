#https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1
#Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def addTwoLists(self, num1, num2):
        # code here

        def reverse_list(node):

            prev = None
            curr = node

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev
        
        reverse_num1 = reverse_list(num1)
        reverse_num2 = reverse_list(num2)

        dummy = Node(-1)
        list_sum = dummy        
        carry = 0

        r1 = reverse_num1
        r2 = reverse_num2

        while r1 and r2:
            n1 = r1.data
            n2 = r2.data
            sum = n1 + n2 + carry
            if sum > 9:
                carry = sum // 10
            else:
                carry = 0
            curr_sum = Node(sum%10)     
            list_sum.next = curr_sum      
            list_sum = list_sum.next

            r1 = r1.next
            r2 = r2.next

        while r1:
            n1 = r1.data            
            sum = n1 + carry            
            if sum > 9:
                carry = sum // 10
            else:
                carry = 0
            curr_sum = Node(sum%10)     
            list_sum.next = curr_sum      
            list_sum = list_sum.next
            r1 = r1.next
        
        while r2:            
            n2 = r2.data
            sum = n2 + carry
            if sum > 9:
                carry = sum // 10
            else:
                carry = 0
            curr_sum = Node(sum%10)     
            list_sum.next = curr_sum      
            list_sum = list_sum.next            
            r2 = r2.next

        if carry:
            curr_sum = Node(carry)     
            list_sum.next = curr_sum      
            list_sum = list_sum.next     
            
        dummy = reverse_list(dummy.next)

        final_sum = dummy

        while final_sum :
            if final_sum.data == 0:
                final_sum = final_sum.next
            else:
                return final_sum




s=Solution()
# num1 = Node(4)
# num1.next = Node(5)
num1 = Node(9)
num1.next = Node(9)
# num1.next.next = Node(6)
# num1.next.next.next = Node(3)

num2 = Node(1)
# num2.next = Node(7)
# num2.next.next = Node(5)

hd = s.addTwoLists(num1, num2)

while hd:
    print(hd.data, end=" ")
    hd = hd.next