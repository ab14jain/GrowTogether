from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        def isValid(r,c,m,n):
            return r >= 0 and r < m and c >= 0 and c < n

        m = len(isWater)
        n = len(isWater[0])
        queue = deque()
        visited = [[0]*n for _ in range(m)]
        level = [[0]*n for _ in range(m)]


        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append([i,j])
                    visited[i][j] = 1
                    
        height = 0
        while queue:
            size = len(queue)
            height += 1
            dir = [-1,0,1,0,-1]
            while size > 0:

                cord = queue.popleft()
                x = cord[0]
                y = cord[1]

                for i in range(4):
                    newX = x + dir[i]
                    newY = y + dir[i+1]
                    if isValid(newX,newY,m,n) and not visited[newX][newY]:
                        queue.append([newX,newY])
                        level[newX][newY] = height
                        visited[newX][newY] = 1

                size -= 1
        
        return level

s=Solution()
   
print(s.highestPeak([[0,1],[0,0]]))
print(s.highestPeak([[0,0,1],[1,0,0],[0,0,0]]))