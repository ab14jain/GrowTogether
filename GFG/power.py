#https://www.geeksforgeeks.org/problems/powx-n/1
import sys
sys.set_int_max_str_digits(1000000)
class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here

        if e == 0:
            return 1
        
        if e < 0:
            return 1 / self.power(b, -e)
        
        temp = self.power(b, (e//2))

        if e%2 == 0:
            return temp * temp
        else:
            return temp * temp * b
    
s=Solution()
print(s.power(.55,3))
print(s.power(-0.67,-7))
print(s.power(34,10000))
        
