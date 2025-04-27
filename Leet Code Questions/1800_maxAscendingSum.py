from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        n = len(nums)
        max_sum = nums[0]
        curr_sum = nums[0]
        for i in range(1, n):

            if nums[i-1] < nums[i]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]
            
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
    
s=Solution()
print(s.maxAscendingSum([10]))
print(s.maxAscendingSum([12,11]))
print(s.maxAscendingSum([10,10,10]))
print(s.maxAscendingSum([10,20,30,5,10,50]))
print(s.maxAscendingSum([10,20,30,40,50]))
print(s.maxAscendingSum([12,17,15,13,10,11,12]))

