from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        twos = deque()
        ones = 0
        m = len(grid)
        n = len(grid[0])

        def isvalid(x,y):
            return x >= 0 and x < m and y >= 0 and y < n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    twos.append([i,j,0])
                    grid[i][j] = 3
                if grid[i][j] == 1:
                    ones += 1 

        if ones == 0:
            return 0
        
        ans = 0
        while twos:
            i,j,t = twos.popleft()
            
            ans = t
            dir = [1,0,-1,0,1]
            for k in range(4):
                x = i + dir[k]
                y = j + dir[k+1]
                if isvalid(x,y):                    
                    if grid[x][y] == 1:
                        twos.append([x,y,t+1])
                        grid[x][y] += 1
                        ones -= 1
        
        if ones == 0:
            return ans

        return -1