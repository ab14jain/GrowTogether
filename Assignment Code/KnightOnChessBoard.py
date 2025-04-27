#https://www.scaler.com/academy/mentee-dashboard/class/325388/homework/problems/292?navref=cl_tt_nv

from collections import deque


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer
    def knight(self, A, B, C, D, E, F):


        def bfs(m, n, sr, sc, dr, dc, visited):
            q = deque()
            q.append([sr,sc])

            while q:
                x,y = q.popleft()   

                if x == dr and y == dc:
                    return visited[x][y]
                
                visited[x][y] = visited[x][y] + 1

                dir_x = [2,2,1,-1,-2,-2,1,-1]
                dir_y = [1,-1,2,2,1,-1,-2,-2]
                for i in range(8):
                    new_x = x + dir_x[i]
                    new_y = y + dir_y[i]

                    if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                        if visited[new_x][new_y] == 0:
                            q.append([new_x,new_y])
                            visited[new_x][new_y] = visited[x][y]

            return -1
            
        visited = [[0]*B for _ in range(A)]            
        ans = bfs(A,B,C-1,D-1,E-1,F-1,visited)
                    
        return ans
    

s=Solution()
print(s.knight(8,8,1,1,8,8))
# print(s.knight(2,4,2,1,4,4))

