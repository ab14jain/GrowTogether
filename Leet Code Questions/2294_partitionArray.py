from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        

        nums.sort()

        i = 0
        j = 0
        n = len(nums)
        count = 0
        while j < n:

            if nums[j] - nums[i] > k:
                i = j
                count += 1
            
            j += 1
        
        return count+1
    
s=Solution()
print(s.partitionArray([3,6,1,2,5], 2))
print(s.partitionArray([1,2,3], 1))
print(s.partitionArray([2,2,4,5], 0))


