from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        max_len = 1
        n = len(nums)
        dp = [1]*n

        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                    
                    if max_len < dp[i]:
                        max_len = dp[i]

        return max_len

        # TLE 22 / 55 testcases passed
        # max_len = 1
        # n = len(nums)
        # def solve(i, arr, prev):

        #     if i >= n:
        #         nonlocal max_len
        #         max_len = max(max_len, len(arr)) 
        #         return  

            
        #     if prev == -1 or prev < nums[i]:
        #         arr.append(nums[i])
        #         take = solve(i+1, arr, nums[i])
        #         arr.pop()

        #     not_take = solve(i+1, arr, prev)

        # solve(0, [], -1)
        # return max_len


s=Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(s.lengthOfLIS([0,1,0,3,2,3]))
print(s.lengthOfLIS([7,7,7,7,7,7,7]))