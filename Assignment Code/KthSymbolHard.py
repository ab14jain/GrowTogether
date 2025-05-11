#https://www.scaler.com/academy/mentee-dashboard/class/325380/homework/problems/31788?navref=cl_tt_nv

from math import ceil
import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : integer
    # @param B : long
    # @return an integer
    def solve(self, A, B):
        
        def kth_small(n, k):

            # 1 -> 0
            # 2 -> 0 1
            # 3 -> 01 10
            # 4 -> 0110 1001
            # 5 -> 01101001 10010110

            if n == 1:
                return 0
            

            prev = kth_small(n-1, ceil(k/2))

            if prev == 0:            
                if k % 2 == 0:
                    return 1
                else:
                    return 0
            else:
                if k % 2 == 0:
                    return 0
                else:
                    return 2

        return kth_small(A,B)


s=Solution()
print(s.solve(2, 1))
print(s.solve(1, 0))
print(s.solve(59701,294634972693719732))
print(s.solve(31508,152124112712823874))