from typing import Counter


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:

        counter = Counter(arr1)
        res = []
        
        for num in arr2:            
            res.extend([num] * counter[num])   
            del counter[num]

        for num in sorted(counter.keys()):
            res.extend([num] * counter[num])     
            
        return res
    
s=Solution()

# print(s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6])) # [2,2,2,1,4,3,3,9,6,7,19]
print(s.relativeSortArray([2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31],[2,42,38,0,43,21])) # [2,2,2,1,4,3,3,9,6,7,19]