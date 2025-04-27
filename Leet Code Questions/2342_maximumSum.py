from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        

        def digit_sum(num):
            s = 0

            while num > 0:
                s += num%10

                num //= 10

            return s
        
        h_map = {}
        max_sum_pair = -1
        for i in range(len(nums)):
            d_sum = digit_sum(nums[i])

            if d_sum in h_map:
                max_sum_pair = max(max_sum_pair, (h_map[d_sum]+nums[i]))
                if nums[i] > h_map[d_sum]:
                    h_map[d_sum] = nums[i]
            else:
                h_map[d_sum] = nums[i]

        return max_sum_pair
                
                
s=Solution()
print(s.maximumSum([18,43,36,13,7]))