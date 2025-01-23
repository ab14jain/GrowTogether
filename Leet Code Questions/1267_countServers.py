
from collections import deque
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        # def isValid(r,c,m,n):
        #     return r >= 0 and r < m and c >= 0 and c < n

        # m = len(grid)
        # n = len(grid[0])
        # # q = deque()
        # stack = []
        # visited = [[0]*n for _ in range(m)]
        # level = [[0]*n for _ in range(m)]

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             stack.append([i,j])
        #             # visited[i][j] = 1
        #             level[i][j] = 1

        # print(visited)
        # max_server = float('-inf')
        # while stack:
        #     # size = len(q)            
        #     # cord = q.popleft()
        #     cord = stack.pop()
        #     x= cord[0]
        #     y= cord[1]
        #     dir = [-1,0,1,0,-1]
        #     # while size:
        #     for i in range(4):
        #         newX = x + dir[i]
        #         newY = y + dir[i+1]

        #         if isValid(newX,newY,m,n) and not visited[newX][newY] and grid[newX][newY] == 1:
        #             server_count = level[newX][newY] + 1
        #             level[newX][newY] = server_count
        #             visited[newX][newY] = 1
        #             max_server = max(max_server, server_count)
        #             stack.append([newX,newY])
                
        #         # size -= 1
        
        # print(level)
        # return max_server

        m = len(grid)
        n = len(grid[0])
        rows = [0]*m
        cols = [0]*n
        total_servers = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
                    total_servers += 1       
        
        for i in range(m):
            for j in range(n):                
                if grid[i][j] == 1 and rows[i] < 2 and cols[j] < 2:
                    total_servers -= 1

        return total_servers         


s=Solution()
print(s.countServers([[1,0],[0,1]]))
print(s.countServers([[1,0],[1,1]]))
print(s.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))