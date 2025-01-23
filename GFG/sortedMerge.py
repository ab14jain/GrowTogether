#https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1


# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def sortedMerge(self,head1, head2):
        # code here       
        if head2 is None:
            return head1

        if head1 is None:
            return head2
        
        if head1.data <= head2.data:
            head1.next = self.sortedMerge(head1.next, head2)
            return head1
        else:
            head2.next = self.sortedMerge(head1, head2.next)
            return head2

        # first_node = Node(-1)
        # merged_head = first_node
        # while head1 and head2:
        #     if head1.data <= head2.data:                
        #         merged_head.next = Node(head1.data) 
        #         head1 = head1.next
        #     else:                
        #         merged_head.next = Node(head2.data) 
        #         head2 = head2.next

        #     merged_head = merged_head.next

        # while head1: 
        #     merged_head.next = Node(head1.data)  
        #     merged_head = merged_head.next
        #     head1 = head1.next           

        # while head2: 
        #     merged_head.next = Node(head2.data)
        #     merged_head = merged_head.next
        #     head2 = head2.next

        # return first_node.next

def printList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

s = Solution()
head1 = Node(5)
head1.next = Node(10)
head1.next.next = Node(15)
head1.next.next.next = Node(40)

head2 = Node(2)
head2.next = Node(3)
head2.next.next = Node(20)
head2.next.next.next = Node(24)

mhead = s.sortedMerge(head1, head2)

printList(mhead)