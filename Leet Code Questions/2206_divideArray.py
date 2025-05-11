from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:        

        n = len(nums)
        if n % 2 == 1:
            return False
        
        nums_map = Counter(nums)
        pairs = n // 2

        count = 0

        for key in nums_map:
            if nums_map[key] % 2 == 0:
               count += (nums_map[key] // 2)
        
        if count == pairs:
            return True
        
        return False
    
s=Solution()
print(s.divideArray([3,2,3,2,2,2]))
print(s.divideArray([1,2,3,4]))
print(s.divideArray([1,1]))


