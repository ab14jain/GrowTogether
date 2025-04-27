#https://www.scaler.com/academy/mentee-dashboard/class/325374/assignment/problems/4697?navref=cl_tt_nv

from collections import deque


class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):


        def dijkstra(grid, src, dest):
            dist = [[float('inf')]*n for _ in range(m)]
            dist[src[0]][src[1]] = 0
            q = deque()

            q.append([0, src[0], src[1]])

            while q:
                d,x,y = q.popleft()
                dir = [1,0,-1,0,1] 
                for i in range(4):
                    new_x = x #+ dir[i]
                    new_y = y #+ dir[i+1]
                    distance = 0
                    while new_x+dir[i] >= 0 and new_x+dir[i] < m and new_y+dir[i+1] >= 0 and new_y+dir[i+1] < n and grid[new_x+dir[i]][new_y+dir[i+1]] == 0:
                        new_x = new_x + dir[i]
                        new_y = new_y + dir[i+1]
                        distance += 1

                    
                    if dist[new_x][new_y] > dist[x][y] + distance:
                        dist[new_x][new_y] = dist[x][y] + distance
                        q.append([dist[new_x][new_y], new_x, new_y])
            
            if dist[dest[0]][dest[1]] == float('inf'):
                return -1
            return dist[dest[0]][dest[1]]
        

        m = len(A)
        n = len(A[0])

        return dijkstra(A, B, C)
        # count = 1
        # graph = [[-1]*n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if A[i][j] == 0:
        #             graph[i][j] = count
        #             count += 1

        # print(graph)

s=Solution()
print(s.solve([[1,1,0,1],[0,0,0,1],[1,0,0,1],[0,0,1,0]], [1,1], [2,1]))
print(s.solve([[0, 0],[0, 0]], [0,0], [0,1]))