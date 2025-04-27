from collections import defaultdict
import math


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        vw_ratio = []
        n = len(A)
        for i in range(n):
            vw_ratio.append((round(A[i]/B[i],2), A[i], B[i]))
        
        vw_ratio.sort(reverse=True)

        max_val = 0
        for i in range(n):
            ratio, val, wei = vw_ratio[i]
            if wei <= C:
                max_val += val
                C -= wei
            else:
                max_val += ratio*C*100
                C = 0     
                break    
        # max_val = max_val
        # max_val_n = int(max_val)        
        return math.floor(max_val)

s=Solution()
# print(s.solve([16,3,3,6,7,8,17,13,7],[3,10,9,18,17,17,6,16,13],11))
# print(s.solve([60, 100, 120],[10, 20, 30],50))
print(s.solve([3],[20],17))
