#https://www.scaler.com/academy/mentee-dashboard/class/325360/homework/problems/1243/?navref=cl_pb_nv_tb
import heapq


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        min_heap = []
        k = 3
        n = len(A)
        ans = [-1]*n
        prod = 1
        for i in range(min(k,n)):
            prod *= A[i]
            if i == k-1:
                ans[i] = prod
                           
            heapq.heappush(min_heap, A[i])

        
        for i in range(min(k,n), n):
            
            if min_heap[0] < A[i]:
                min_num = heapq.heappop(min_heap)
                prod = prod // min_num
                prod *= A[i]
                ans[i] = prod
                heapq.heappush(min_heap, A[i])
            else:
                ans[i] = prod

        return ans
s=Solution()
print(s.solve([5]))
print(s.solve([1,2,3,4,5]))
print(s.solve([10,2,13,4]))
print(s.solve([10,20,13,5,3,12,2,14,1]))

