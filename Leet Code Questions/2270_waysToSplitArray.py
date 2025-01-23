class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:

        n = len(nums)

        prefix_sum = [0]*n

        for i in range(n):
            if i == 0:
                prefix_sum[i] = nums[i]
            else:
                prefix_sum[i] = prefix_sum[i-1]+nums[i]

        last = prefix_sum[n-1]
        count = 0
        for i in range(n-1):
            first_half = prefix_sum[i]
            second_half = last - first_half
            if first_half >= second_half:
                count += 1
        
        return count
        

s=Solution()
print(s.waysToSplitArray([1,2,2,2,5,0])) # 3
print(s.waysToSplitArray([0,3,3])) # 1
print(s.waysToSplitArray([3,2,1])) # 0