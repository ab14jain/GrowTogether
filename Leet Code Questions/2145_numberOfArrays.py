from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        n = len(differences)
        count = 0
        for i in range(lower, upper+1):

            arr = [i]

            for j in differences:
                nxt = arr[-1] + j
                if lower <= nxt <= upper: 
                    arr.append(nxt)
                else:
                    break
            
            if len(arr) == n+1:
                count += 1
        return count
    
s=Solution()
print(s.numberOfArrays([1,-3,4], 1, 6))
print(s.numberOfArrays([3,-4,5,1,-2], -4, 5))
print(s.numberOfArrays([4,-7,2], 3,6))