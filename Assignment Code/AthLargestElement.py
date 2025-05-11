#https://www.scaler.com/academy/mentee-dashboard/class/325360/assignment/problems/989?navref=cl_tt_nv
import heapq


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):

        min_heap = []
        n = len(B)
        ans = [0]*n
        
        for i in range(A):
            heapq.heappush(min_heap, B[i])
            if i != A-1:
                ans[i] = -1
            else:
                ans[i] = min_heap[0]
            
            # if len(min_heap) < A:
            #     ans.append(-1)
            # else:                
            #     while min_heap:
            #         if min_heap[0] <= 
            #         item = heapq.heappop(min_heap) 
            #         ans.append(item)                        
            #         break

        for i in range(A, n):

            if B[i] <= min_heap[0]:
                ans[i] = min_heap[0]
            else:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, B[i])
                ans[i] = min_heap[0]

        return ans
    
s=Solution()
print(s.solve(4, [1,2,3,4,5,6]))
print(s.solve(2, [15,20,99,1]))

                