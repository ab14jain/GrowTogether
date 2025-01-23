import heapq


class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        
        rows = len(heightMap)
        cols = len(heightMap[0])

        if rows < 3 or cols < 3:
            return 0

        visited = [[False for _ in range(cols)] for _ in range(rows) ]
        min_heap = []       

        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows-1 or j == 0 or j == cols-1):
                    heapq.heappush(min_heap, [heightMap[i][j], i , j])
                    visited[i][j] = True
        

        water_level = 0
        trapped_water = 0
        directions = [-1,0,1,0,-1] #URDL

        while min_heap:
            curr_height = heapq.heappop(min_heap)

            height = curr_height[0]
            r = curr_height[1]
            c = curr_height[2]

            water_level = max(water_level, height)

            for i in range(4):
                newR = r + directions[i]
                newC = c + directions[i+1]

                if ((newR >= 0 and newR < rows and newC >= 0 and newC < cols) 
                    and not visited[newR][newC]):

                    visited[newR][newC] = True
                    heapq.heappush(min_heap, [heightMap[newR][newC],newR, newC])

                    if heightMap[newR][newC] < water_level:
                        trapped_water += (water_level - heightMap[newR][newC]) 

        return trapped_water
    


s=Solution()

print(s.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
print(s.trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))