from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        o_index = 10000                
        for i in range(n):
            if nums[i] == 0:
                o_index = i
                break

        for i in range(n-1):
            if nums[i] == nums[i+1] and nums[i] != 0:
                nums[i] *= 2
                nums[i+1] = 0                
                o_index = min(o_index, i+1)      
        
        
        if o_index == -1:
            return nums
        
        i = o_index
        j = i+1
        while j < n:
            if nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i = i+1
            j += 1

        return nums
    
s=Solution()
print(s.applyOperations([328,0,0,0,93,43,802,802,0,580,0,0,0,973,0,0,774]))
print(s.applyOperations([847,847,0,0,0,399,416,416,879,879,206,206,206,272]))