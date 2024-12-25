import heapq


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        
        min_heap = []
        n = len(nums)
        for i in range(n):
            heapq.heappush(min_heap, [nums[i],i])
        

        while k > 0:            
            top = heapq.heappop(min_heap)
            top[0] *= multiplier
            heapq.heappush(min_heap, top)
            k -= 1

        min_heap.sort(key = lambda x : x[1])
        min_heap = [x[0] for x in min_heap]

        return min_heap
        


s = Solution()
print(s.getFinalState([1,2,3,4,5], 3, 2)) # [1,2,3,4,5]