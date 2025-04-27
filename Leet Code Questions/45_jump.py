from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0]*n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            one_step = 1 + dp[i+1]
            index_step = 0

            if i + nums[i] >= n-1:
                index_step = 1
            else:
                # index_step = dp[i + nums[i]] + 1
                index_step = min(dp[(i+1):(i+nums[i]+1)])+1
            
            dp[i] = min(one_step, index_step)
        
        return dp[0]
    
s=Solution()
print(s.jump([4,1,1,3,1,1,1]))
print(s.jump([2,3,1,1,4]))
        