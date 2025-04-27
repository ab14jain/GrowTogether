from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique_ele = set(nums)
        unique_count = len(unique_ele)
        
        l = 0
        r = 0
        n = len(nums)
        freq = {}
        subarr_count = 0
        
        while l < n:
            while r < n and len(freq) < unique_count:
                freq[nums[r]] = freq.get(nums[r], 0) + 1
                r += 1
            
            if len(freq) < unique_count:
                break
            
            subarr_count += n - r + 1            
            
            freq[nums[l]] -= 1
            if freq[nums[l]] == 0:
                del freq[nums[l]]
            l += 1
        
        return subarr_count