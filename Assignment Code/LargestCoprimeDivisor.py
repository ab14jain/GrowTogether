#https://www.scaler.com/academy/mentee-dashboard/class/325294/homework/problems/358?navref=cl_tt_nv

import math
import sys
sys.setrecursionlimit(10**6)

class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def cpFact(self, A, B):

            # def gcd(A, B):
            #     if B == 0:
            #         return A
            #     return gcd(B, A % B)           
            
            # def factors(A):
            #     factors = []
            #     for i in range(1, int(A**0.5)+1):
            #         if A % i == 0:
            #             factors.append(i)
            #             factors.append(A//i)
            #     return factors  

            # all_factors = factors(A)
            # all_factors.sort()

            # for i in range(len(all_factors)-1, -1, -1):                
            #     if gcd(B, all_factors[i]) == 1:
            #         return all_factors[i]
			
            # def gcd(A, B):
            #     if A == 0 or B == 0:
            #         return 0
                
            #     if A == B:
            #         return A

            #     if A > B:
            #         return gcd(A-B, B)

            #     return gcd(A, B-A)           
                

            # while gcd(A,B) != 1:
            #     A = A / gcd(A,B)

            # return int(A)
			
            def gcd(A, B):
                if max(A, B) % min(A, B) == 0:
                    return min(A, B)
                return gcd(min(A, B), max(A, B) % min(A, B))
        

            while gcd(A,B) != 1:
                A = A / gcd(A,B)

            return int(A)
     

s = Solution()
print(s.cpFact(30, 12)) # 5
print(s.cpFact(90, 47)) # 90
print(s.cpFact(348816241, 564364410)) # 348816241
print(s.cpFact(886326226, 513319290)) # 443163113
print(s.cpFact(14629248, 832779840)) # 1411
print(s.cpFact(5, 10)) # 1
print(s.cpFact(2, 2)) # 1   