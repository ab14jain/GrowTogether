from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        

        i = 0
        j = 1
        n = len(nums)

        if n == 1:
            return True
        
        while j < n:

            if ((nums[i] % 2 == 0 and nums[j] % 2 == 0) or 
            (nums[i] % 2 == 1 and nums[j] % 2 == 1)):
                return False
            i += 1
            j += 1
            
        return True
    

s=Solution()
print(s.isArraySpecial([1]))
print(s.isArraySpecial([2,1,4]))
print(s.isArraySpecial([4,3,1,6]))
print(s.isArraySpecial([4,3,2,7]))