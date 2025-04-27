#https://www.scaler.com/academy/mentee-dashboard/class/325306/homework/problems/6707/?navref=cl_pb_nv_tb

import math


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        k = 1
        count = 0
        while k <= math.sqrt(2*A):
            calc = A - (k*(k-1))//2
            if calc % k == 0:
                count += 1   
            k += 1
        
        return count


s=Solution()
print(s.solve(15))
print(s.solve(25))