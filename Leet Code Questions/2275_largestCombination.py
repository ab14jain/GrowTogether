from math import log2
import math


class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        
        candidates_count = 0
        max_bit = math.floor(log2(max(candidates))) + 1
        for i in range(max_bit):
            count = 0
            for num in candidates:
                if num & (1 << i):
                    count += 1
            candidates_count = max(candidates_count, count)
        
        return candidates_count
    
s= Solution()
print(s.largestCombination([2,3,5,7])) # 3
print(s.largestCombination([9,8,7,6,5,4,3,2,1])) # 5
print(s.largestCombination([1,2,4,8])) # 1
print(s.largestCombination([1,2,4,8,16])) # 1
print(s.largestCombination([1,2,4,8,16,32])) # 1