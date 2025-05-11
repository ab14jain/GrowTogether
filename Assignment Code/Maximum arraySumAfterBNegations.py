import heapq


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        min_heap = []

        for i in range(len(A)):
            heapq.heappush(min_heap, A[i])

        
        while B:
            num = heapq.heappop(min_heap)
            heapq.heappush(min_heap, -num)
            B -= 1

        return sum(min_heap)
    
s=Solution()
print(s.solve([24, -68, -29, -9, 84], 4))
print(s.solve([57, 3, -14, -87, 42, 38, 31, -7, -28, -61], 10))