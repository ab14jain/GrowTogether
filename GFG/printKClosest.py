#https://www.geeksforgeeks.org/problems/k-closest-elements3619/1

import heapq


class Solution:
    def printKClosest(self, arr, k, x):
        # code here

        n=len(arr)
        min_heap = []

        for i in range(n):

            if len(min_heap) < k and x != arr[i]:
                heapq.heappush(min_heap, arr[i])
            else:
                curr = min_heap[0]

                if abs(curr-x) > abs(arr[i]-x) and x != arr[i]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, arr[i])

                
        return min_heap


s=Solution()
print(s.printKClosest([1, 3, 4, 10, 12], 2, 4))
print(s.printKClosest([12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56], 4, 35))