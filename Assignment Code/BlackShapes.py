#https://www.scaler.com/academy/mentee-dashboard/class/325388/homework/problems/291/?navref=cl_pb_nv_tb
from collections import deque


class Solution:
	# @param A : list of strings
	# @return an integer
	def black(self, A):
            
            m = len(A)
            n = len(A[0])
            visited = [[False]*n for _ in range(m)]

            def bfs(r,c,visited):
                
                q = deque()
                q.append([r,c])

                while q:
                    x,y = q.popleft()

                    if visited[x][y]:
                        continue

                    visited[x][y] = True
                    dir = [1,0,-1,0,1]
                    for i in range(4):
                        new_x = x + dir[i]
                        new_y = y + dir[i+1]

                        if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                            if A[new_x][new_y] == 'X':
                                q.append([new_x,new_y])

            count = 0
            for i in range(m):
                for j in range(n):                    
                    if A[i][j] == 'X' and not visited[i][j]:
                        count += 1
                        bfs(i,j,visited)
                        
            return count
            # while X:
            #     x,y = X.pop()

            #     if visited[x][y]:
            #         continue

            #     visited[x][y] = True
            #     dir = [1,0,-1,0,1]
            #     for i in range(4):
            #         new_x = x + dir[i]
            #         new_y = y + dir[i+1]

            #         if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
            #             if A[new_x][new_y] == 'X':
            #                 X.append([new_x,new_y])
            
            # return visited
    
s=Solution()
print(s.black([ ["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"] ]))
print(s.black([ ["X", "O"], ["O", "X"] ]))