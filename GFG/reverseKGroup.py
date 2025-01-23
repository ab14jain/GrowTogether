#https://www.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1

#Node is defined as

import math


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        # Code here

        # total_node = 0
        # curr = head

        # while curr:
        #     total_node += 1
        #     curr = curr.next

        # times = total_node // k
        
        # prev = None
        # last = None
        # curr = head
        # start = curr   

        # start_idx = 0     
        # while times > 0:
        #     count = k 
        #     curr = head
        #     for _ in range(start_idx):
        #         curr = curr.next 
        #         prev = start

        #     while count > 0:
        #         next = curr.next
        #         last = next                
        #         curr.next = prev
        #         prev = curr
        #         curr = next                
        #         count -= 1           
            
        #     head = prev           
        #     start_idx += k
        #     times -= 1

        # return head

        def reverseKNode(node, start, end):
            
            if not node or start == end:
                return node
            
            start_prev = None
            last_node = None

            curr = node
            count = 0
            while curr and count < start:
                start_prev = curr
                curr = curr.next
                count += 1

            while curr and count < end:
                curr = curr.next
                last_node = curr
                count += 1
            
            
            if start_prev:
                curr = start_prev.next
                prev = last_node if last_node else None
            else:
                curr = node
                prev = last_node if last_node else None
            
            times = k

            while curr and times > 0:

                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

                times -= 1

            if start_prev:
                start_prev.next = prev  
            else:
                node = prev  
        
            return node
        
        total_node = 0
        curr = head

        while curr:
            total_node += 1
            curr = curr.next

        times = math.ceil(total_node / k )
        start_idx = 0
        end_idx = start_idx + k
        while times:
            head = reverseKNode(head, start_idx , end_idx)
            start_idx += k
            end_idx = min(start_idx + k, total_node)
            times -= 1

        return head
    
        while head:
            print(head.data, end=" ")
            head = head.next
                                                                                                                                                                                                                                                                                                                                                                                   
s=Solution()
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
# head.next.next.next.next.next.next.next.next = Node(9)

hd = s.reverseKGroup(head, 3)

while hd:
    print(hd.data, end=" ")
    hd = hd.next
        
