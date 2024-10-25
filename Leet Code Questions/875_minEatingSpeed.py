import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:       
        
        left = 1
        right = max(piles)
        min_k = right
        while left <= right:
            mid = (left + right )// 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)

            if time <= h:
                min_k = min(min_k,mid)
                right = mid - 1
            else:
                left = mid + 1
        return min_k

# Time complexity: O(nlogn)
# Space complexity: O(1)
s = Solution()
print(s.minEatingSpeed([3,6,7,11], 8))
print(s.minEatingSpeed([30,11,23,4,20], 5))



        