import math
from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        # def count_factors(num):
        #     count = 0
        #     for i in range(1,math.ceil(math.sqrt(num))+1):
        #         #for j in range(1, num+1):                    
        #         if num % i == 0:                    
        #             if i == num/i:
        #                 count += 1
        #             else:
        #                 count += 2
        #     return count

        
        # primes = []
        # min_diff = float('inf')
        # ans = [-1,-1]
        # prev_prime = -1
        # for i in range(left, right+1):
        #     if count_factors(i) == 2:
        #         primes.append(i)
        #         if prev_prime != -1:
        #             if (i - prev_prime) < min_diff:
        #                 min_diff = (i - prev_prime)
        #                 ans = [prev_prime, i]
        #         prev_prime = i
                
        
        # # if min_diff == float('inf'): 
        # #     return [-1,-1] 
        
        # return ans

        shieves = [True]*(right+1)

        shieves[0] = False
        shieves[1] = False

        for i in range(2, math.ceil(math.sqrt(right))+1):
            for j in range(i*i, right+1, i):
                shieves[j] = False

        
        min_diff = float('inf')
        ans = [-1,-1]
        prev_prime = -1
        for i in range(left, right+1):
            if shieves[i]: 
                if prev_prime != -1:
                    if (i - prev_prime) < min_diff:
                        min_diff = (i - prev_prime)
                        ans = [prev_prime, i]
                prev_prime = i
        
        return ans
        
s = Solution()
print(s.closestPrimes(10, 19))
print(s.closestPrimes(4,6))
