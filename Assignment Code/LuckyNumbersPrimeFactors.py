#https://www.scaler.com/academy/mentee-dashboard/class/325296/homework/problems/1095?navref=cl_tt_nv

import math


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        primes = [0]*(A+1)  
        for i in range(2, A+1):
            if primes[i] == 0:
                for j in range(1, math.ceil((A+1)/i)):                
                    primes[i*j] += 1
            
        
        return primes.count(2)
        

        

s=Solution()
print(s.solve(8))
print(s.solve(12))