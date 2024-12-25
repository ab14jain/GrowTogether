# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/?envType=daily-question&envId=2024-11-21
class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:

        def mark_gaurded_cell(row,col,grid):
            #left Iteration
            for i in range(col-1,-1,-1):
                if grid[row][i] == 2 or grid[row][i] == 3:
                    break
                grid[row][i] = 1
            
            # Right Iteration
            for i in range(col+1,n,1):
                if grid[row][i] == 2 or grid[row][i] == 3:
                    break
                grid[row][i] = 1
            
            # Up Iteration
            for i in range(row-1,-1,-1):
                if grid[i][col] == 2 or grid[i][col] == 3:
                    break
                grid[i][col] = 1
            
            # Down Iteration
            for i in range(row+1,m,1):
                if grid[i][col] == 2 or grid[i][col] == 3:
                    break
                grid[i][col] = 1

        grid = [[0]*n for _ in range(m)]
        
        for g in guards:
            r,c = g
            grid[r][c] = 2
        
        for w in walls:
            r,c = w
            grid[r][c] = 3
        
        for i in range(len(guards)):
            r,c = guards[i]
            mark_gaurded_cell(r,c,grid)

        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
        
        return count    
    
    
# Time complexity: O(m*n)
# Space complexity: O(m*n)

s=Solution()
print(s.countUnguarded(4,6,[[0,0],[1,1],[2,3]],[[0,1],[2,2],[1,4]])) # 7
print(s.countUnguarded(2,7,[[1,5],[1,1],[1,6],[0,2]],[[0,6],[0,3],[0,5]])) # 1
print(s.countUnguarded(8,9,[[5,8],[5,5],[4,6],[0,5],[6,5]],[[4,1]])) # 25
print(s.countUnguarded(3,3,[[0,0],[0,2]],[[1,1],[1,2]])) # 2
print(s.countUnguarded(3,3,[[0,0],[0,2]],[[1,1],[1,2],[0,1]])) # 2
print(s.countUnguarded(3,3,[[0,0],[0,2]],[[1,1],[1,2],[0,1],[2,2]])) # 1
print(s.countUnguarded(3,3,[[0,0],[0,2]],[[1,1],[1,2],[0,1],[2,2],[2,1]])) # 0
        