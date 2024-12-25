#https://www.scaler.com/academy/mentee-dashboard/class/313152/assignment/problems/26930?navref=cl_tt_nv
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        bin_rep = list(bin(A)[2:])
        calc = (A | (1 << B))
        if A == calc:
            A = A ^ (1 << B)
        return A


# Driver code
s = Solution()
print(s.solve(49, 0)) # 48
print(s.solve(28, 1)) # 28
print(s.solve(10, 2)) # 14
print(s.solve(10, 3)) # 10
print(s.solve(10, 4)) # 10
print(s.solve(10, 5)) # 42
