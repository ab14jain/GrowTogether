class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        
        n = len(nums)
        if n < 3:
            return 0
        
        i = 0
        j = 0
        count = 0
        while j < n:
            while j+1 < n and nums[j+1] - nums[j] == nums[j] - nums[j-1]:
                j += 1
            
            count += (j-i)*(j-i-1)//2
            i = j
            j += 1
        
        return count

# Time complexity: O(n)
# Space complexity: O(1)

s=Solution()
print(s.numberOfArithmeticSlices([1,2,3,4])) # 3
print(s.numberOfArithmeticSlices([1,2,3,4,5])) # 6
print(s.numberOfArithmeticSlices([1,2,3,4,5,6])) # 10
