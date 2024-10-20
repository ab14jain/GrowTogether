import math


class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n <= 0:
           return False
        
        factors = self.getFactors(n)
        print(factors)
        for i in factors:
            if i > 5 and self.isPrime(i):
                return False
            
            
        return True
    
    def isPrime(self, n: int) -> bool:
        if n == 1:
            return False
        
        if self.getFactors(n).__len__() > 2:
            return False

        return True

    def getFactors(self, n: int) -> list:
        factors = []
        
        for i in range(1, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                factors.append(i)
                factors.append(n // i)

        factors = list(set(factors)) 

        
        return factors

s= Solution()
print(s.isUgly(14))  # True