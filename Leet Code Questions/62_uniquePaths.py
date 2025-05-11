class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # Bracktracking will TLE for large number of m,n
        # count = 0
        # def print_path(s_r, s_c, d_r, d_c):     
        #     nonlocal count      
        #     if s_r == d_r-1 and s_c == d_c-1:
        #         count += 1                    
            
        #     if s_r < m - 1:
        #         print_path(s_r+1, s_c, d_r, d_c)
            
        #     if s_c < n - 1:
        #         print_path(s_r, s_c+1, d_r, d_c)

        # print_path(0,0,m,n)

        # return count


        dp = [[0]*n for _ in range(m)]

        for i in range(n):
            dp[m-1][i] = 1

        for i in range(m):
            dp[i][n-1] = 1

        
        for r in range(m-2, -1, -1):
            for c in range(n-2,-1,-1):
                dp[r][c] = dp[r+1][c]+dp[r][c+1]
        
        return dp[0][0]
        
        
    
s=Solution()
print(s.uniquePaths(3,7))
print(s.uniquePaths(3,2))
print(s.uniquePaths(13,7))
print(s.uniquePaths(23,12))