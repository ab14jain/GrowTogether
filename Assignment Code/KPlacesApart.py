import heapq


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

        min_heap = []
        n = len(A)

        if n == 1:
            return A
        
        for i in range(B+1):
            heapq.heappush(min_heap, A[i])

        id = 0

        for i in range(B+1, n):
            A[id] = heapq.heappop(min_heap)
            id += 1
            heapq.heappush(min_heap, A[i])

        while min_heap:
            A[id] = heapq.heappop(min_heap)
            id += 1
    
        return A
    

s=Solution()
print(s.solve([2,1,17,10,21,95], 1))
