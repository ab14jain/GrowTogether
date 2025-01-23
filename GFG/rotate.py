#https://www.geeksforgeeks.org/problems/rotate-a-linked-list/1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here

        node_count = 0
        curr = head
        prev = None
        while curr:
            prev = curr
            curr = curr.next
            node_count += 1        

        if k >= node_count:
            k = k % node_count

        if k != 0:
            prev.next = head
        
        curr = head
        while curr and k > 1:             
            curr = curr.next
            k -= 1

        if k != 0:
            head = curr.next
            curr.next = None       

        return head
    

s=Solution()

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

hd = s.rotate(head, 6)