#https://www.scaler.com/academy/mentee-dashboard/class/325296/assignment/problems/35398?navref=cl_tt_nv

import math


class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):

        is_prime = [True]*(A+1)

        is_prime[0] =  False
        is_prime[1] =  False

        for i in range(2,math.ceil(math.sqrt(A)+1)):
            x = i
            for j in range(i*i, A+1, i):
                is_prime[j] = False
        
        result = []

        for i in range(len(is_prime)):
            if is_prime[i]:
                result.append(i)
        
        return result


s=Solution()
print(s.solve(49))
# print(s.solve(1))
# print(s.solve(7))
# print(s.solve(12))
# print(s.solve(1000000))