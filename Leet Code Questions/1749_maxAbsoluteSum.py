from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        # n = len(nums)
        # max_sum = float('-inf')
        # min_sum = float('inf')
        # curr_sum = 0      

        # for i in range(n):            
        #     curr_sum += nums[i]
        #     max_sum = max(curr_sum, max_sum)
        #     if curr_sum < 0:
        #         curr_sum = 0  

        # curr_sum = 0
        # for i in range(n):            
        #     curr_sum += nums[i]
        #     min_sum = min(curr_sum, min_sum)

        #     if curr_sum > 0:
        #         curr_sum = 0

        # return max(abs(max_sum), abs(min_sum))

        n = len(nums)
        max_sum = 0
        min_sum = 0
        prefix_sum = 0     

        for i in range(n):            
            prefix_sum += nums[i]

            if prefix_sum > 0:
                max_sum = max(prefix_sum, max_sum)

            if prefix_sum < 0:
                min_sum = min(prefix_sum, min_sum)

        return max_sum-min_sum
            

s=Solution()
print(s.maxAbsoluteSum([2,-5,1,-4,3,-2]))