# https://www.scaler.com/academy/mentee-dashboard/class/325306/assignment/problems/68?navref=cl_tt_nv

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):

        ans = [[0] *A for _ in range(A)]
        for i in range(A):
            for j in range(i+1):
                if j == 0 or j == i:
                    ans[i][j] = 1
                else:
                    ans[i][j] = ans[i-1][j-1] + ans[i-1][j] 
        
        return ans

s=Solution()
print(s.solve(10))