import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        heap = []

        for num in nums:            
            heapq.heappush(heap, num)

        nops = 0
        while heap:
            first = heapq.heappop(heap)
            
            if first >= k:
                break
            
            second = heapq.heappop(heap)
            calc = min(first, second) * 2 + max(first, second)            
            heapq.heappush(heap, calc)
            
            nops += 1
        
        return nops

s=Solution()
print(s.minOperations([19,44,61,96,84,79,84,61,97,44],44))
print(s.minOperations([2,11,10,1,3],10))
print(s.minOperations([2,1,2,4,9],20))
print(s.minOperations([2,2,2],6))


