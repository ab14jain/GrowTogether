from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        mp = {
            0:0,
            1:0,
            2:0
        }
        n = len(nums)

        for i in range(n):
            mp[nums[i]] += 1

        i = 0

        for j in range(3):            
            c = mp[j] 
            while c:
                nums[i] = j
                c -= 1
                i += 1
        
        return nums
    
s=Solution()
print(s.sortColors([2,0,2,1,1,0]))
print(s.sortColors([2,0,1]))

            
