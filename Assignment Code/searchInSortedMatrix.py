class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        m = len(A[0])
        i = 0
        j = m - 1
        min_val = float('Inf')
        while (j > -1 and i < n):
            if A[i][j] == B:
                min_val = min(min_val,(i + 1)* 1009 + (j + 1))
                j -= 1
            elif A[i][j] < B:
                i += 1
            elif A[i][j] > B:
                j -= 1
                i = 0

        if min_val == float('Inf'):
            return -1
        return min_val


s = Solution()
# print(s.solve([[1],[1]], 1)) # 1
# print(s.solve([[1, 2], [3, 3]], 4)) # 2019
# print(s.solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2)) # 1011
print(s.solve([[1, 2, 4], [1, 2, 5], [1, 2, 3]], 3)) # 1011
# print(s.solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5)) # 5