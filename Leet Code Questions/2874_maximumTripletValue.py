from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = float('-inf')

        # TLE 563 / 599 testcases passed
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             max_val = max(max_val, (nums[i]-nums[j])*nums[k])

        
        # if max_val < 0:
        #     return 0
        
        # return max_val

        # prefix_max = [float('-inf')]*n
        suffix_max = [float('-inf')]*n

        # prefix_max[0] = nums[0]
        suffix_max[n-1] = nums[n-1]

        # for i in range(1, n):
        #     prefix_max[i] = max(nums[i], prefix_max[i-1])
        
        for i in range(n-2, -1, -1):
            suffix_max[i] = max(nums[i], suffix_max[i+1])
        
        left_max = nums[0]
        for i in range(1, n-1):
            max_val = max(max_val, (left_max - nums[i])*suffix_max[i+1])
            left_max = max(left_max, nums[i])
        return max_val

s=Solution()
print(s.maximumTripletValue([12,6,1,2,7]))
            