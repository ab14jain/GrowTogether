class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        
        n = len(nums)
        if n == 0:
            return 0
        
        if n == 1:
            return 1 if nums[0] >= target else 0
        
        i = 0
        j = 0
        min_len = float('inf')
        sum_val = 0
        while j < n:
            sum_val += nums[j]
            
            while sum_val >= target:
                min_len = min(min_len, j - i + 1)
                sum_val -= nums[i]
                i += 1
                
            j += 1
            
        return min_len if min_len != float('inf') else 0
    
# Time complexity: O(n)
# Space complexity: O(1)

s=Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3])) # 2
print(s.minSubArrayLen(4, [1,4,4])) # 1
