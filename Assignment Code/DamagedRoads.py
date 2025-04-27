#https://www.scaler.com/academy/mentee-dashboard/class/325388/homework/problems/6284?navref=cl_tt_nv

from collections import defaultdict
import heapq


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):

        m = len(A)
        n = len(B)        
        MOD = 1000000007
        min_heap = []        
        for i in range(m):
            heapq.heappush(min_heap, [A[i],1])
        
        for i in range(n):
            heapq.heappush(min_heap, [B[i],0])

        
        total_cost = 0
        r = m+1
        c = n+1
        while min_heap:
            cost, dir = heapq.heappop(min_heap)
            
            if dir == 1:  
               total_cost += c*cost             
               r -= 1
            else:
                total_cost += r*cost  
                c -= 1

        return total_cost%MOD



s=Solution()
print(s.solve([1,1,1], [1,1,2]))
print(s.solve([1,2,3], [4,5,6]))