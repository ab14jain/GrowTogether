#https://www.scaler.com/academy/mentee-dashboard/class/325296/homework/problems/297/?navref=cl_pb_nv_tb
import math


class Solution:
	# @param A : integer
	# @return a list of integers
	def primesum(self, A):
		
            prime_factor = set()

            n = math.ceil(math.sqrt(A))
            shieve = [True]*(A + 1)
            shieve[0] = False
            shieve[1] = False

            for i in range(2,n+1):
                for j in range(i*i, A+1, i):
                    shieve[j] = False 
                  
            for i in range(len(shieve)):
                if shieve[i]:
                    prime_factor.add(i)

            prime_factor = sorted(prime_factor)
            for pf in prime_factor:
                if (A - pf) in prime_factor:
                    return [pf, A-pf]
                

s=Solution()
print(s.primesum(4))
# print(s.primesum(3423456))
