class Solution:
    def subarraySum(self, nums: list[int]) -> int:

        n = len(nums)
        prefix_sum = [0]*n
        prefix_sum[0] = nums[0]

        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        total_sum = 0
        for i in range(n):
            start = max(0, i-nums[i])

            if start == 0:
                total_sum += prefix_sum[i]
            else:
                total_sum += (prefix_sum[i] - prefix_sum[start-1])

        return total_sum

s = Solution()
print(s.subarraySum([2]))
print(s.subarraySum([2,3,1]))
print(s.subarraySum([3,1,1,2]))