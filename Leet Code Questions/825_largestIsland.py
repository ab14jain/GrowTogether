from collections import defaultdict
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        n = len(grid)        
        dir = [-1,0,1,0,-1]
        def is_valid(r, c):
            return r >= 0 and r < n and c >= 0 and c < n
        
        def dfs(grid, r, c, island_size_map, id):           

            
            count = 1
            grid[r][c] = id
            for i in range(4):
                new_r = r + dir[i]
                new_c = c + dir[i+1]
                if is_valid(new_r, new_c) and grid[new_r][new_c] == 1:
                    count += dfs(grid, new_r, new_c, island_size_map, id)

            return count       
        
        
        island_size_map = defaultdict(int)

        UID = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:                    
                    island = dfs(grid,i,j,island_size_map,UID)
                    island_size_map[UID] = island
                    UID += 1

        max_island_size = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0: 
                    
                    islands = set(0)
                    for k in range(4):
                        new_r = i + dir[k]
                        new_c = j + dir[k+1]

                        if is_valid(new_r,new_c):                            
                            islands.add(grid[new_r][new_c])

                    count = 1
                    for iland in islands:
                        count += island_size_map[iland]

                    max_island_size = max(max_island_size, count)

        return n*n if max_island_size == 0 else max_island_size

s = Solution()
print(s.largestIsland([[1,0,1],[0,0,1],[1,0,1]]))