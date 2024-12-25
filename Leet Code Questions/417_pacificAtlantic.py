class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        
        n = len(heights)
        m = len(heights[0])
        
        directions = [-1, 0, 1, 0, -1]
        def dfs(x, y, visited):
            visited[x][y] = True
            for i in range(4):
                x_dir, y_dir = x + directions[i], y + directions[i + 1]
                if 0 <= x_dir < n and 0 <= y_dir < m and not visited[x_dir][y_dir] and heights[x_dir][y_dir] >= heights[x][y]:
                    dfs(x_dir, y_dir, visited)
        
        pacific = [[False] * m for _ in range(n)]
        atlantic = [[False] * m for _ in range(n)]
        
        for i in range(n):
            dfs(i, 0, pacific)
            dfs(i, m - 1, atlantic)
        
        for i in range(m):
            dfs(0, i, pacific)
            dfs(n - 1, i, atlantic)
        
        res = []
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res

s=Solution()

