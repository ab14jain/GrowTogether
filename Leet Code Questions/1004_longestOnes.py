from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        n = len(nums)
        zero_count = 0
        window_size = 0
        ans = 0
        while j < n:   
            if nums[j] == 0:
                zero_count += 1 

            while zero_count > k:
                if nums[i] == 0:
                    zero_count -= 1

                window_size -= 1
                i += 1 

            window_size += 1

            if ans < window_size:
                ans = window_size   

            j += 1   
        
        return ans
    
s = Solution()
print(s.longestOnes([0], 0))
print(s.longestOnes([0], 1))
print(s.longestOnes([1], 0))