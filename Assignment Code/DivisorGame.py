#https://www.scaler.com/academy/mentee-dashboard/class/325294/homework/problems/2126?navref=cl_tt_nv

import math


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        # def gcd(A, B):
        #     if max(A, B) % min(A, B) == 0:
        #         return min(A, B)
        #     return gcd(min(A, B), max(A, B) % min(A, B))
    

        # gcd_f = math.gcd(B,C)
        # count = 0
        # prod = B*C
        # if gcd_f == 1:  
        #     while prod <= A:
        #         count += 1
        #         if prod <= A:                    
        #             prod = B*C*(count+1)
                    
        # else:
        #     x = 1            
        #     lcm  = (B*C)//gcd_f           
        #     while lcm <= A:
        #         lcm = gcd_f * x   
        #         if lcm >= B and lcm >= C and lcm%B == 0 and lcm%C == 0:
        #             count += 1
        #         x += 1 
                
        # return count

        def gcd(A, B):           
            if B == 0:
                return A
            
            return gcd(B, A%B)

        
        lcm = (B * C)// gcd(B, C)
        return A//lcm
    # 6816621
    # 8157697

s = Solution()
print(s.solve(546456345,234,324))
print(s.solve(5000000,24,72))
print(s.solve(500,7,13))
print(s.solve(30,9,15))
print(s.solve(200,24,36))
