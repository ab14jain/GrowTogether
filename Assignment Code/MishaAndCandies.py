import heapq
import math


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        candies_eaten = 0
        heap = []
        n = len(A)

        # Time Complexity O(n)
        for i in range(n):
            heapq.heappush(heap, A[i])

        while heap:
            candies = heapq.heappop(heap)
            if(candies <= B):
                eaten = candies//2
                candies_eaten += eaten
                rem  = candies - eaten
                if heap:
                    next_candies = heapq.heappop(heap)
                    heapq.heappush(heap, next_candies+rem)
            else:
                break

        return candies_eaten
    
s=Solution()
print(s.solve([3,2,3],4))
print(s.solve([1,2,1],2))

        