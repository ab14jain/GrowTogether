import math
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1000000007
        fives = math.ceil(n/2)
        fours = n - fives

        def pow(num, ex):

            if ex == 0:
                return 1

            half = pow(num, ex//2)
            
            if ex % 2 == 1:
                return half*half*num%MOD

            return half*half%MOD       
        
        
        return pow(5, fives)%MOD * pow(4, fours)%MOD

s=Solution()
print(s.countGoodNumbers(1))
print(s.countGoodNumbers(2))
print(s.countGoodNumbers(3))
print(s.countGoodNumbers(4))
print(s.countGoodNumbers(5))
print(s.countGoodNumbers(6))
print(s.countGoodNumbers(7))
print(s.countGoodNumbers(78))
print(s.countGoodNumbers(784564654))
print(s.countGoodNumbers(78456465445675))
print(s.countGoodNumbers(10000000000))
print(s.countGoodNumbers(100000000000))
print(s.countGoodNumbers(1000000000000))
print(s.countGoodNumbers(10000000000000))
print(s.countGoodNumbers(1000000000000000))
print(s.countGoodNumbers(53346575675))
print(s.countGoodNumbers(345345345345345))
print(s.countGoodNumbers(897898786786))
print(s.countGoodNumbers(99999999999999))