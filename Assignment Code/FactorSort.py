from functools import cmp_to_key
import math
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        def factor_count (num):

            fact_count = 0
            factors = []
            sq_root = math.ceil(math.sqrt(num))
            for i in range(1, sq_root+1):
                if num == i * i:
                    factors.append(i)
                elif num % i == 0:
                    factors.append(i)
                    factors.append(num//i)
            fact_count = len(set(factors))
            return fact_count

        def factor_count_sort(a,b):

            if factor_count(a) < factor_count(b):
                return -1
            elif factor_count(b) < factor_count(a):
                return 1
            else: 
                if a < b:
                    return -1
                elif b < a:
                    return 1
                else:
                    return 0

            
        
        A.sort(key=cmp_to_key(factor_count_sort))

        return A

s=Solution()
# A=[5, 2, 9, 3, 5, 7, 1]
# print(s.solve(A)) # Output: [1, 2, 3, 5, 5, 7, 9]

#A=[10000,6,8,9,12,100]
A=[12,44]
print(s.solve(A)) # Output: [1, 2, 3, 4, 5]