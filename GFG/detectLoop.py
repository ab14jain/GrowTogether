#https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1


# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
	

# Return boolean value True or False

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here

        # Time Complexity - O(n)
        # Space Complexity - O(n)

        # is_visited = {}
        # curr = head
        # pos = 0
        # has_loop = False        
        # while curr:
        #     if curr in is_visited:
        #         has_loop = True
        #         break
        #     else:
        #         pos += 1
        #         is_visited[curr] = pos 
                
        #     curr = curr.next     
        
        # return has_loop

        #Using Floyd's Cycle Two pointer fast and slow

        slow = head
        fast = head

        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                return True 

        return False
    
s=Solution()
head = Node(1)
head.next = Node(8)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head.next

hd = s.detectLoop(head)
print(hd)