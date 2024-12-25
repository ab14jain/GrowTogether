#https://www.scaler.com/academy/mentee-dashboard/class/325310/homework/problems/5697?navref=cl_tt_nv
from bisect import bisect_left
from math import gcd


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        lcm = (B * C) // gcd(B, C)
        left = 0
        right = lcm * A

        # We run a loop until left is less than right 

        while left < right: 
            mid = (left + right) // 2

            num = (mid // B) + (mid // C) - (mid // lcm)            
            if num < A: 
                left = mid + 1
            else: 
                right = mid        

        return left % (1000000000 + 7)
        
        # MOD = 10**9 + 7
        # def lcm(x, y):
        #     return x * y // gcd(x, y)
        
        # lcm_of_b_c = lcm(B, C)
        # r = (B + C) * A

        # Ath_magical = bisect_left(range(r), A, key=lambda x: x // B + x // C - x // lcm_of_b_c)

        # return Ath_magical % MOD

        # ans = []
        # i = 1
        # multiple = 1
        # seen = set()
        # while i < A:

        #     if B*multiple not in seen and C*multiple not in seen:
        #         if B*multiple < C*multiple:
        #             ans.append(B*multiple)
        #             ans.append(C*multiple)
        #         else:
        #             ans.append(C*multiple)
        #             ans.append(B*multiple)
                
        #         seen.add(B*multiple)
        #         seen.add(C*multiple)
            
        #         i += 2
        #     multiple += 1

        # return ans[-1]


s= Solution()
print(s.solve(2, 3, 3)) #6
print(s.solve(2, 3, 4)) #4
print(s.solve(5, 2, 3)) #4
print(s.solve(19, 11, 13)) #117