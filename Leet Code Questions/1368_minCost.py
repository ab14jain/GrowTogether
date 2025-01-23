from collections import deque
import heapq
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:   

        direction = {
            1: [0, 1],
            2: [0, -1],
            3: [1, 0],
            4: [-1, 0]
        }

        row, col = len(grid), len(grid[0])
        q = deque([(0, 0, 0)])
        min_cost = {(0,0):0}

        while q:
            x, y, cost = q.popleft()
            if (x, y) == (row-1, col-1):
                return cost

            for d in direction:
                dr, dc = direction[d]
                nr, nc = x + dr, y + dc
                n_cost = cost if d == grid[x][y] else cost + 1

                if (nr < 0 or nc < 0 or nr == row or nc == col or
                n_cost >= min_cost.get((nr, nc), float('inf'))):
                    continue
                
                min_cost[(nr, nc)] = n_cost
                if d == grid[x][y]:
                    q.appendleft((nr, nc, n_cost))
                else:
                    q.append((nr, nc, n_cost))