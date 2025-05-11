#https://www.scaler.com/academy/mentee-dashboard/class/325348/homework/problems/19

from collections import deque


class Solution:
	# @param A : list of list of integers
	# @return an integer
	def minPathSum(self, A):
            m = len(A)
            n = len(A[0])           

            def recur(x, y):
                
                if not (x >= 0 and x < m and y >= 0 and y < n):
                    return 0
                
                if x == m-1 and y == n-1:
                    return A[x][y]

                right = A[x][y] + recur(x, y+1)
                down = A[x][y] + recur(x+1, y)

                return min(right, down)

            # def bfs(node):                  
            #     q = deque()
            #     q.append(node)

            #     while q:
            #         x,y = q.popleft()
            #         direction = [1,0,-1,0,1]
            #         for i in range(4):
            #             nex_x = x + direction[i]
            #             nex_y = y + direction[i+1]

            #             if nex_x >= 0 and nex_x < m and nex_y >= 0 and nex_y < n:
            #                 if not visited[nex_x][nex_y]:
            #                     q.append([nex_x, nex_y])
            #                     visited[nex_x][nex_y] = True



            # return bfs([0,0])