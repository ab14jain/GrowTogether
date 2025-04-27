from typing import List
import sys
sys.set_int_max_str_digits(1000000)

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        

        digit = int("".join(map(str,b)))
        mod = 1337
        def pow(num, p):

            if p == 0:
                return 1
            
            temp = pow(num, p//2)

            if p % 2 == 0:
                return temp*temp%mod
            else:
                return num*temp*temp%mod
        
        if a == 1:
            return 1
        return pow(a,digit)

s=Solution()
# print(s.superPow(2,[3]))
# print(s.superPow(2,[1,3]))
print(s.superPow(1,[4,3,3,8,5,2]))
print(s.superPow(2,[4,3,3,8,5,2]))