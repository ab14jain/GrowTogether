#https://www.scaler.com/academy/mentee-dashboard/class/325352/assignment/problems/1302?navref=cl_tt_lst_nm

from collections import defaultdict


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        h_map = defaultdict(int)
        n = len(A)
        min_distant = float('inf')
        for i in range(n):
            if A[i] in h_map:
                min_distant = min(min_distant, i - h_map[A[i]])

            h_map[A[i]] = i

        if min_distant == float('inf'):
            return -1
        
        return min_distant
    
s=Solution()
print(s.solve([7,1,3,4,1,7]))
print(s.solve([7,1,3,4,1,7,7]))
print(s.solve([1,1]))
