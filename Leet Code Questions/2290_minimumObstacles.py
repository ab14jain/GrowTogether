#https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/?envType=daily-question&envId=2024-11-28
class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = [(0, 0, 0)]
        visited = set()
        visited.add((0, 0))
        while q:
            x, y, obs = q.pop(0)
            if x == n - 1 and y == m - 1:
                return obs
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    if grid[nx][ny] == 1:
                        q.append((nx, ny, obs + 1))
                    else:
                        q.insert(0, (nx, ny, obs))
        return -1

s=Solution()
print(s.minimumObstacles([[0,0,0],[1,1,0],[1,1,0]])) # 1
print(s.minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]])) # 0
print(s.minimumObstacles([[0,1,1],[1,1,0],[1,1,0]])) # 2

        