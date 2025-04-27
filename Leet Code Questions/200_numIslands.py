class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:        
        def dfs(x,y,c):
            
            grid[x][y] = c

            stack = []
            stack.append([x,y])

            while stack:
                i,j= stack.pop()

                dir_x = [-1, 0, 0, 1]; 
                dir_y = [0,-1, 1, 0]; 

                for k in range(4):
                    new_x = i + dir_x[k]
                    new_y = j + dir_y[k]

                    if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and grid[new_x][new_y] == '1':
                        grid[new_x][new_y] = c
                        stack.append([new_x,new_y])
            
        

        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j,count)
                    count += 1
        
        return count