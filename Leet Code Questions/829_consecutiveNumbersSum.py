import math


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        k = 1
        count = 0
        while k <= math.sqrt(2*n):
            calc = n - (k*(k-1))//2
            if calc % k == 0:
                count += 1   
            k += 1
        
        return count