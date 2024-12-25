from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1
        
        heap = []

        for key, value in d.items():
            if len(heap) < k or heap[0][0] < value:
                heapq.heappush(heap, [value, key])            
            if len(heap) > k:
                heapq.heappop(heap)           
        
        
        return [x[1] for x in heap]
s = Solution()
print(s.topKFrequent([1,1,1,2,2,3,4,5,5,5,5,5,5,4,4,4,4], 2)) # [1,2]
print(s.topKFrequent([1], 1)) # [1]
print(s.topKFrequent([1,2], 2)) # [1,2]
print(s.topKFrequent([1,2,2,3,3,3], 2)) # [3,2]