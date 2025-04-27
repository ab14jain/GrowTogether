#https://www.scaler.com/academy/mentee-dashboard/class/325360/homework/problems/4950?navref=cl_tt_nv

import heapq


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        min_heap = []
        
        m = len(A)
        n = len(A[0])
        B = B - 1
        for i in range(m):
            for j in range(n):                
                heapq.heappush(min_heap, A[i][j])
                
        
        while B > 0:
            heapq.heappop(min_heap)
            B -= 1
        return min_heap[0]
    
s=Solution()
print(s.solve([[9, 11, 15],[10, 15, 17]], 6))
print(s.solve([[5, 9, 11],[9, 11, 13],[10, 12, 15],[13, 14, 16],[16, 20, 21]], 12))
print(s.solve([[5, 9, 11],[9, 11, 13],[10, 12, 15],[13, 14, 16],[16, 20, 21]], 10))
print(s.solve([[5, 9, 11],[9, 11, 13],[10, 12, 15],[13, 14, 16],[16, 20, 21]], 3))