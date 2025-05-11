from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        # unique_path_count = 0
        # def shortest_path(mat, src_r, src_c, dest_r, dest_c, distance, visited):
            
        #     if src_r < 0 or src_r >= m or src_c < 0 or src_c >= n:
        #         return

        #     if mat[src_r][src_c] == 1 or visited[src_r][src_c]:
        #         return
            
        #     nonlocal unique_path_count
        #     if src_r == dest_r and src_c == dest_c:         
        #         unique_path_count += 1
            
                
        #     visited[src_r][src_c] = True
        #     shortest_path(mat, src_r+1, src_c, dest_r, dest_c, distance+1, visited)
        #     shortest_path(mat, src_r-1, src_c, dest_r, dest_c, distance+1, visited)           
                
            
          
        #     shortest_path(mat, src_r, src_c+1, dest_r, dest_c, distance+1, visited)
        #     shortest_path(mat, src_r, src_c-1, dest_r, dest_c, distance+1, visited)
        #     visited[src_r][src_c] = False


        # visited = [[False]*n for _ in range(m)]
        # shortest_path(obstacleGrid, 0, 0, m-1, n-1, 0,visited)
        # return unique_path_count

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]

        for i in range(n):
            dp[m-1][i] = 1

        for i in range(m):
            dp[i][n-1] = 1

        
        for r in range(m-2, -1, -1):
            for c in range(n-2,-1,-1):
                if (obstacleGrid[r+1][c] == 0 ):
                    dp[r][c] += dp[r+1][c] 
                if (obstacleGrid[r][c+1] == 0 ):
                    dp[r][c] += dp[r][c+1]
        
        return dp[0][0]
    

s=Solution()
print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))