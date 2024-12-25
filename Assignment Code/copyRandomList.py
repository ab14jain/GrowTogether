#https://www.scaler.com/academy/mentee-dashboard/class/325316/assignment/problems/159?navref=cl_tt_lst_nm
# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):

        next_random_map = {}
        curr = head
        if not curr:
            return None       
        
        head_copy = None
        curr_copy = head_copy

        while curr:
            
            if not head_copy:
                curr_copy = RandomListNode(curr.label)
                head_copy = curr_copy
            else:
                curr_copy.next = RandomListNode(curr.label)
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

s=Solution()
head = RandomListNode(1)
head.next = RandomListNode(2)
head.next.next = RandomListNode(3)
head.random = head.next.next
head.next.random = head
head.next.next.random = head


def print_list(head):
    curr = head
    while curr:
        print(curr.label, end=' ')
        print(curr.random.label, end=' ')
        curr = curr.next
    print()

print_list(head)


# head.next.next.next.next = RandomListNode(5)
# head.next.next.next.random = RandomListNode(1)
# head.next.next.next.next.next = RandomListNode(6)
# head.next.next.next.next.random = RandomListNode(5)
# head.next.next.next.next.next.next = RandomListNode(7)
# head.next.next.next.next.next.random = RandomListNode(3)
# head.next.next.next.next.next.next.next = RandomListNode(8)
# head.next.next.next.next.next.next.random = RandomListNode(6)
# head.next.next.next.next.next.next.next.next = RandomListNode(9)
# head.next.next.next.next.next.next.next.random = RandomListNode(8)
# head.next.next.next.next.next.next.next.next.next = RandomListNode(10)
# head.next.next.next.next.next.next.next.next.random = RandomListNode(9)

print(s.copyRandomList(head))
