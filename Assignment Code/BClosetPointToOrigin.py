from functools import cmp_to_key
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        distance = 0

        def distant_sort(a,b):
            d1 = ((a[0])**2 + (a[1])**2)**.5
            d2 = ((b[0])**2 + (b[1])**2)**.5

            if d1 < d2:
                return -1
            elif d1 > d2:
                return 1
            else:
                return 0
        
        A.sort(key=cmp_to_key(distant_sort))

        result = A[0:B]

        return result

s= Solution()
print(s.solve([[1, -1],[2, -1]] , 1)) #[[1, 3]]
print(s.solve([[1, 3], [-2, 2]], 1)) #[[1, 3]]
print(s.solve([[1, 3], [-2, 2], [5, 8]], 2)) #[[1, 3], [-2, 2]]