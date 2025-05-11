import heapq


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):


        min_heap = []
        n = len(A)
        for i in range(n):
            heapq.heappush(min_heap, A[i])

        cost = 0
        while min_heap and len(min_heap) > 1:
            first = heapq.heappop(min_heap)
            second = heapq.heappop(min_heap)

            cost += first + second
            heapq.heappush(min_heap, first+second)

        return cost
    
s=Solution()
print(s.solve([1,2,3,4,5]))
print(s.solve([5,17,100,11]))
        