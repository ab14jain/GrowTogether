
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


from typing import Optional


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:

        next_random_map = {}
        curr = head
        if not curr:
            return None       
        
        head_copy = None
        curr_copy = head_copy

        while curr:
            
            if not head_copy:
                curr_copy = Node(curr.val)
                head_copy = curr_copy
            else:
                curr_copy.next = Node(curr.val)
                curr_copy = curr_copy.next

            next_random_map[curr] = curr_copy  

            curr = curr.next

        
        curr = head
        curr_copy = head_copy
        while curr:

            if curr.random:
                curr_copy.random = next_random_map[curr.random]
            else:
                curr_copy.random = None
            curr = curr.next
            curr_copy = curr_copy.next
        
        return head_copy


