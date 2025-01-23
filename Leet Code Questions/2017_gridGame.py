from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        prefix_arr = [[0 for _ in range(n)] for _ in range(m)]             
        r = 0
        for j in range(n):                
            if j == 0:
                prefix_arr[r][j] = grid[r][j]
            else:
                prefix_arr[r][j] = prefix_arr[r][j-1] + grid[r][j]
        
        r = 1
        for j in range(n-1, -1, -1):    
            if j == n-1:
                prefix_arr[r][j] = grid[r][j]
            else:         
                prefix_arr[r][j] = prefix_arr[r][j+1] + grid[r][j]

        row1_sum = prefix_arr[0][n-1]
        row2_sum = prefix_arr[1][0]

        min_points = float('inf')
        for i in range(n):            
            not_collected_points = max(row1_sum - prefix_arr[0][i],row2_sum - prefix_arr[1][i])
            min_points = min(min_points,not_collected_points)

        return min_points


s = Solution()
print(s.gridGame([[2,5,4],[1,5,1]]))
print(s.gridGame([[3,3,1],[8,5,2]]))
print(s.gridGame([[1,3,1,15],[1,3,3,1]]))