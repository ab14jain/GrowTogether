from collections import deque


class Solution:
	def orangesRotting(self, mat):
		#Code here

            fresh_oranges = 0            
            q = deque()
            m = len(mat)
            n = len(mat[0])
            for i in range(m):
                for j in range(n):
                    
                    if mat[i][j] == 2:
                        q.append([i,j])
                        mat[i][j] = 3
                    
                    if mat[i][j] == 1:
                        fresh_oranges += 1

            if fresh_oranges == 0:
                return 0
            
            count = 0

            while q:   
                size = len(q)
                count += 1
                while size:            
                    x,y = q.popleft()
                    dir = [1,0,-1,0,1]
                    
                    for i in range(4):
                        new_x = x + dir[i]
                        new_y = y + dir[i+1]

                        if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                            if mat[new_x][new_y] == 1:
                                mat[new_x][new_y] = 3
                                fresh_oranges -= 1
                                q.append([new_x,new_y])

                        if fresh_oranges == 0:
                            return count
                    
                    size -= 1
                
            
            return -1
    
s=Solution()
print(s.orangesRotting([[0, 1, 2], [0, 1, 2], [2, 1, 1]]))