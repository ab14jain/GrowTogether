import math
from typing import List


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime_factor = set()
        pf_sum = []
        sq_n = math.ceil(math.sqrt(n))
        shieve = [True]*(n + 1)
        shieve[0] = False
        shieve[1] = False

        for i in range(2,sq_n+1):
            for j in range(i*i, n+1, i):
                shieve[j] = False 
                
        for i in range(len(shieve)):
            if shieve[i]:
                prime_factor.add(i)

        prime_factor = sorted(prime_factor)
        seen = set()
        j = len(prime_factor)//2
        for k in range(j+1):
            pf = prime_factor[k]
            if (n - pf) in prime_factor:
                seen.add(pf)
                seen.add(n-pf)
                factors = [pf, n-pf]                
                
                pf_sum.append(factors)

        return pf_sum
    

s=Solution()
print(s.findPrimePairs(1000000))
print(s.findPrimePairs(10))
print(s.findPrimePairs(2))
                