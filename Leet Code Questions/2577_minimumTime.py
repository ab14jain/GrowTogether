#https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/?envType=daily-question&envId=2024-11-29

import heapq


class Solution:
    def minimumTime(self, grid: list[list[int]]) -> int:
        
        #solve this
        n = len(grid)
        m = len(grid[0])
        
        
        directions = [-1, 0, 1, 0, -1]
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 + grid[0][0] and grid[1][0] > 1 + grid[0][0]:
            return -1

        visited = [[False] * n for _ in range(m)]
        min_heap = [(0, 0, 0)] 
        visited[0][0] = True

        while min_heap:
            time, x, y = heapq.heappop(min_heap)

            if x == m - 1 and y == n - 1:
                return time

            for i in range(4):
                x_dir, y_dir = x + directions[i], y + directions[i + 1]
                if 0 <= x_dir < m and 0 <= y_dir < n and not visited[x_dir][y_dir]:
                    visited[x_dir][y_dir] = True
                    time_count = time + 1
                    if grid[x_dir][y_dir] > time_count:
                        time_count = grid[x_dir][y_dir] if (grid[x_dir][y_dir] - time) % 2 == 1 else grid[x_dir][y_dir] + 1
                    heapq.heappush(min_heap, (time_count, x_dir, y_dir))

        return -1
    
    
s=Solution()
print(s.minimumTime([[1,1],[1,1]])) # 2
print(s.minimumTime([[1,3],[3,2]])) # 3
print(s.minimumTime([[1,2,2],[3,2,3],[1,2,1]])) # 7
print(s.minimumTime([[1,2,3],[3,2,1]])) # 4
print(s.minimumTime([[1,2,1],[1,2,1]])) # 3
print(s.minimumTime([[1,1,1],[1,1,1]])) # 2