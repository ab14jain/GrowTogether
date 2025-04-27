#https://www.scaler.com/academy/mentee-dashboard/class/325352/assignment/problems/168773?navref=cl_tt_nv

import heapq


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):


        B.sort()
        min_heap = []

        heapq.heappush(min_heap, B[0][1])
        
        for i in range(1,A):
            s, e = B[i]
            if min_heap and s >= min_heap[0]:
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, e)

        return len(min_heap)
s=Solution()
print(s.solve(3, [[0, 30],[5, 10],[15, 20]]))
print(s.solve(1, [[0, 1]]))
print(s.solve(6, [[454,523],[28,78],[59,153],[639,651],[404,491],[180,273]]))