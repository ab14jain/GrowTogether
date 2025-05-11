#https://www.scaler.com/academy/mentee-dashboard/class/325360/assignment/problems/238?navref=cl_tt_nv
# Definition for singly-linked list.
import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):

        min_heap = []
        n = len(A)

        for i in range(n):
            head = A[i]
            if head is not None:
                heapq.heappush(min_heap, (head.val, i, head))

        dummy = ListNode(-1)
        tail = dummy

        while min_heap:
            _, i, top = heapq.heappop(min_heap)

            tail.next = top
            tail = top

            if top.next is not None:
                heapq.heappush(min_heap, (top.next.val, i, top.next))

        return dummy.next
    

k = 3

arr = [None] * k

arr[0] = ListNode(1)
arr[0].next = ListNode(3)
arr[0].next.next = ListNode(5)
arr[0].next.next.next = ListNode(7)

arr[1] = ListNode(2)
arr[1].next = ListNode(4)
arr[1].next.next = ListNode(6)
arr[1].next.next.next = ListNode(8)

arr[2] = ListNode(0)
arr[2].next = ListNode(9)
arr[2].next.next = ListNode(10)
arr[2].next.next.next = ListNode(11)

s = Solution()
head = s.mergeKLists(arr)

