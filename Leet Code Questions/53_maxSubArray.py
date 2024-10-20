class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        maxSum = float('-inf')
        currentSum = 0
        for i in range(len(nums)):
            currentSum += nums[i]

            if currentSum > maxSum:
                maxSum = currentSum
            
            if currentSum < 0:
                currentSum = 0
        
        return maxSum


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6     
print(s.maxSubArray([1])) # 1
print(s.maxSubArray([-1])) # -1

