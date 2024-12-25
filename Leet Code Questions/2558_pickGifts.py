import heapq
import math
class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        # n = len(gifts)

        # while k > 0:
        #     max_pile = max(gifts)
        #     sq = math.floor(math.sqrt(max_pile))
        #     idx = gifts.index(max_pile)

        #     gifts[idx] = sq

        #     k -= 1
        
        # return sum(gifts)  

        i = 0
        heap = [-g for g in gifts]
        heapq.heapify(heap)
        while i < k:
            max_pile = -heapq.heappop(heap)
            sq = math.floor(math.sqrt(max_pile))
            heapq.heappush(heap, -sq)
            i += 1
        
        return sum([-g for g in heap])
    
    
s = Solution()
print(s.pickGifts([1,2,3,4], 1)) # 10
print(s.pickGifts([1,2,3,4], 2)) # 10
print(s.pickGifts([1,2,3,4], 3)) # 10
