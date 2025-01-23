class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dfs(idx, curr_sum):

            if  idx == n:
               if curr_sum == target:
                   return 1
               return 0
            
            key = str(idx) + "_" + str(curr_sum)
            if key in memo:
                return memo[key]

            plus = dfs(idx+1, curr_sum + nums[idx])
            minus = dfs(idx+1, curr_sum - nums[idx])
            memo[key] = plus + minus
            return memo[key]
        
        return dfs(0, 0)
    
# [1,1,1,1,1]

#               1
#           /       \
#          2         0
#         / \       / \
#        3   1     1  -1
#       / \ / \   / \ / \
#      4  2 2  0 2  0 0 -2
#     / \/ \/ \/ \/ \/ \/ \/
#    5  3 3 1 3 1 1 1 -1 1
#   / \/\ /\ /\ /\ /\ /\ /\
#  6  4 4 2 4 2 2 2 0 2 0 0

# Time complexity: O(2^n)
# Space complexity: O(n)
# Runtime: 1020 ms, faster than 36.92% of Python3 online submissions for Target Sum.
# Memory Usage: 14.4 MB, less than 77.09% of Python3 online submissions for Target Sum.

# Approach: Recursion
# The idea is to try every possible combination of + and - for each number in the nums list.
# The base case is when we reach the end of the list, we check if the current sum is equal to the target.
# If it is, we return 1, otherwise we return 0.
# We then return the sum of the number of ways we can reach the target by adding and subtracting the current number.
# We start the recursion from the first number in the list and the current sum as 0.


s=Solution()
print(s.findTargetSumWays([1,1,1,1,1], 3)) #5
print(s.findTargetSumWays([1], 1)) #1
print(s.findTargetSumWays([1,2,3,4,5], 10)) #1
print(s.findTargetSumWays([1,2,3,4,5], 15)) #1
print(s.findTargetSumWays([1,2,3,4,5], 20)) #1
