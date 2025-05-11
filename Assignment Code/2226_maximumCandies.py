from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def isPossible(arr, n):
            count = 0
            
            for c in arr:
                count += c//n
            
            if count >= k:
                return True
            
            return False

        total_candies = sum(candies)

        if total_candies < k:
            return 0
        
        min_candies = 1
        max_candies = max(candies)
        
        l = min_candies
        r = max_candies

        mid = l + (r-l)//2
        max_candies_ans = 0
        while l <= r:
            if isPossible(candies, mid):
                max_candies_ans = mid
                l = mid + 1
            else:
                r = mid - 1
            
            mid = l + (r-l)//2
        
        return max_candies_ans
    
s=Solution()
print(s.maximumCandies([2,5,7,9,2],11))
print(s.maximumCandies([5,8,6],3))