import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        if num == 1:
            return False
        x = math.floor(math.sqrt(num))
        divisors_sum = 0
        while x > 0:
            if num % x == 0:
                f1 = x
                f2 = num // x
                if x == 1 or x * x == num:
                    divisors_sum += f1
                else:
                    divisors_sum += f1
                    divisors_sum += f2

            x -= 1
        
        return True if divisors_sum == num else False
    

s = Solution()
print(s.checkPerfectNumber(100)) # True
print(s.checkPerfectNumber(100000000)) # True
print(s.checkPerfectNumber(28)) # True
print(s.checkPerfectNumber(6)) # True
print(s.checkPerfectNumber(496)) # True
print(s.checkPerfectNumber(8128)) # True
print(s.checkPerfectNumber(2)) # False
print(s.checkPerfectNumber(1)) # False
print(s.checkPerfectNumber(3)) # False
print(s.checkPerfectNumber(4)) # False
print(s.checkPerfectNumber(5)) # False
print(s.checkPerfectNumber(7)) # False
print(s.checkPerfectNumber(8)) # False
print(s.checkPerfectNumber(9)) # False
print(s.checkPerfectNumber(10)) # False
print(s.checkPerfectNumber(11)) # False
print(s.checkPerfectNumber(12)) # False
print(s.checkPerfectNumber(13)) # False
print(s.checkPerfectNumber(14)) # False