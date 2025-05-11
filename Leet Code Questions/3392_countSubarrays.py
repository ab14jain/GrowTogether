from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        n = len(nums)
        i = 0
        j = 2
        count = 0
        while j < n:
            first_last_sum = nums[i]+nums[j]
            mid_sum = nums[(i+j)//2]

            if mid_sum % 2 == 0 and first_last_sum == mid_sum//2:
                count += 1

            i += 1
            j += 1

        return count
    
s=Solution()
print(s.countSubarrays([1,2,1,4,1]))
print(s.countSubarrays([1,2,1,5,1]))
print(s.countSubarrays([1,1,1]))