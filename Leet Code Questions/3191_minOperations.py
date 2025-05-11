from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i] = 1
                if nums[i+1] == 0:
                    nums[i+1] = 1
                else:
                    nums[i+1] = 0
                
                if nums[i+2] == 0:
                    nums[i+2] = 1
                else:
                    nums[i+2] = 0
                
                count += 1

        if nums.count(0) == 0:
            return count
        
        return -1
    

s=Solution()
print(s.minOperations([0,1,1,1,0,0]))
print(s.minOperations([0,1,1,1]))