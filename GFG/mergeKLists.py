#https://www.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1

import heapq


class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class Solution:
    def mergeKLists(self, arr):
        # code here
        # return head of merged list

        min_heap = []
        n = len(arr)
        for i in range(n):
            head = arr[i]
            if head is not None:
                heapq.heappush(min_heap, (head.data, i, head))

        dummy = Node(-1)
        tail = dummy


        while min_heap:
            _, i, top = heapq.heappop(min_heap)

            tail.next = top
            tail = top

            if top.next is not None:
                heapq.heappush(min_heap, (top.next.data, i, top.next))

        return dummy.next
    

getMedian