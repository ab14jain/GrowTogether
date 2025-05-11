from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        #This will give TLE as time complexity will 8^n
        
        # shortest_path_len = float('inf')
        # m = len(grid)
        # n = len(grid[0])

        # def is_valid(r,c):
        #     return r >= 0 and r < m and c >= 0 and c < n
        
        # visited = [[False]*n for _ in range(m)]
        # def shortest_path(mat, s_r, s_c, d_r, d_c, visited, path_len):            
            
        #     nonlocal shortest_path_len
        #     if s_r == d_r and s_c == d_c:
        #         shortest_path_len = min(shortest_path_len, path_len)

        #     if is_valid(s_r, s_c) and mat[s_r][s_c] == 0 and not visited[s_r][s_c]:
        #         visited[s_r][s_c] = True
        #         shortest_path(mat, s_r+1, s_c, d_r, d_c, visited, path_len+1)
        #         shortest_path(mat, s_r-1, s_c, d_r, d_c, visited, path_len+1)
        #         shortest_path(mat, s_r, s_c+1, d_r, d_c, visited, path_len+1)
        #         shortest_path(mat, s_r, s_c-1, d_r, d_c, visited, path_len+1)

        #         shortest_path(mat, s_r+1, s_c+1, d_r, d_c, visited, path_len+1)
        #         shortest_path(mat, s_r-1, s_c-1, d_r, d_c, visited, path_len+1)
        #         shortest_path(mat, s_r+1, s_c-1, d_r, d_c, visited, path_len+1)
        #         shortest_path(mat, s_r-1, s_c+1, d_r, d_c, visited, path_len+1)

        #         visited[s_r][s_c] = False


        # if grid[0][0] == 1 or grid[m-1][n-1] == 1:
        #     return -1
        # shortest_path(grid, 0, 0, m-1, n-1, visited, 0)

        # return shortest_path_len+1 if shortest_path_len != float('inf') else -1

        #Solved uisng BFS

        q = deque()
        q.append([0,0])

        m = len(grid)
        n = len(grid[0])

        if m == 0 or n == 0 or grid[0][0] != 0 or grid[m-1][n-1] != 0:
            return -1

        def is_valid(r,c):
            return r >= 0 and r < m and c >= 0 and c < n
        
        visited = [[False]*n for _ in range(m)] 

        level = 0
        while q:
            size = len(q)            
            while size > 0:
                curr = q.popleft()
                x = curr[0]
                y = curr[1]

                if x == m-1 and y ==n-1:
                    return level+1

                dir = [-1,0,1,0,-1]
                diag_dir = [1,1,-1,-1,1]

                for i in range(4):
                    new_x = x+dir[i]
                    new_y = y+dir[i+1]
                    if is_valid(new_x,new_y) and not visited[new_x][new_y] and grid[new_x][new_y] == 0:
                        q.append([new_x,new_y])
                        visited[new_x][new_y] = True
                
                for i in range(4):
                    new_x = x+diag_dir[i]
                    new_y = y+diag_dir[i+1]
                    if is_valid(new_x,new_y) and not visited[new_x][new_y] and grid[new_x][new_y] == 0:
                        q.append([new_x,new_y])
                        visited[new_x][new_y] = True

                size -= 1

            level += 1

        
        return -1


s=Solution()
# print(s.shortestPathBinaryMatrix([[0,1],[1,0]]))
print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
# print(s.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))