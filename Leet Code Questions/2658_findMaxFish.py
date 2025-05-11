from collections import deque
from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        def isValid(x,y,r,c):
            return x >= 0 and x < r and y >= 0 and y < c
        
        def dfs(mat, visited, r, c, x, y):            
            fish_count =  mat[x][y] 
            for i in range(4):
                newX = x + dir[i]
                newY = y + dir[i+1]

                if isValid(newX,newY,r,c) and not visited[newX][newY] and grid[newX][newY]:                    
                    visited[newX][newY] = True
                    fish_count += dfs(mat,visited,r,c,newX,newY)
                   
            return fish_count           


        dir = [-1,0,1,0,-1]
        r = len(grid)
        c = len(grid[0])        
        visited = [[False]*c for _ in range(r)]
        max_fish = float('-inf')        
        for i in range(r):
            for j in range(c):
                if grid[i][j] != 0 and not visited[i][j]:
                    visited[i][j] = True
                    max_fish = max(max_fish, dfs(grid,visited,r,c,i,j))

        return max_fish
        
        

s=Solution()
print(s.findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))