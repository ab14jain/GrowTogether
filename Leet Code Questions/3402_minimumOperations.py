class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        ops = 0
        for c in range(col):
            for r in range(1, row):
                prev = grid[r-1][c]
                if grid[r][c] <= prev:
                    calc = prev - grid[r][c] + 1
                    grid[r][c] = calc + grid[r][c]
                    ops += calc

        
        return ops
    
s=Solution()
# print(s.minimumOperations([[2,4],[6,8]])) # 2
# print(s.minimumOperations([[1,2],[3,4]])) # 1
# print(s.minimumOperations([[1,3],[3,2]])) # 3
# print(s.minimumOperations([[1,1,1],[1,1,1],[1,1,1]])) # 6
print(s.minimumOperations([[3,2],[1,3],[3,4],[0,1]])) # 15
print(s.minimumOperations([[3,2,1],[2,1,0],[1,2,3]])) # 12


                