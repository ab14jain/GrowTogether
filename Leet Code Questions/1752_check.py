from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        
        n = len(nums)
        rotated_point = 0
        for i in range(1,n):
            if nums[i-1] <= nums[i]:
                continue
            else:                
                rotated_point += 1
        
        if rotated_point > 1:
            return False
        elif rotated_point == 1:
            if nums[n-1] > nums[0]:
                return False
        
        return True
    
s=Solution()
print(s.check([1,1,1]))