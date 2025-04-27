from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        t_sum = sum(nums)
        n = len(nums)
        if t_sum % 2 != 0:
            return False
        
        target_sum = t_sum // 2
        dp = [[-1]*(target_sum+1) for _ in range(n+1)]
        def solve(i, res):

            if i >= n:
                return False
            
            if res == target_sum:
                return True
            
            if res > target_sum:
                return False

            if dp[i][res] != -1:
                return dp[i][res]
            
            inc = solve(i+1, res + nums[i])
            exc = solve(i+1, res)

            dp[i][res] = inc or exc
            return dp[i][res]
        
        return solve(0, 0)

        # nums.sort()  
        
        # l = 0
        # r = n-1

        # while l <= r:
        #     mid = l + (r-l)//2

        #     l_sum = sum(nums[:mid+1])
        #     r_sum = t_sum-l_sum

        #     if l_sum == r_sum:
        #         return True
        #     elif l_sum < r_sum:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        
        # return False

s=Solution()
print(s.canPartition([1,3,4,4]))
print(s.canPartition([1,5,11,5]))
print(s.canPartition([1,2,3,4,5]))
print(s.canPartition([1,2,5]))
            
            