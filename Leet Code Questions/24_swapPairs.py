# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
            
            times = 2

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

        times = total_node // 2
        start_idx = 0
        end_idx = start_idx + 2
        while times:
            head = reverseKNode(head, start_idx , end_idx)
            start_idx += 2
            end_idx = start_idx + 2
            times -= 1

        return head