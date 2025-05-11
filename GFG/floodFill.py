from collections import deque


class Solution:
	def floodFill(self, image, sr, sc, newColor):
		#Code here
		
            m = len(image)
            n = len(image[0])

            def bfs(cord):                  
                q = deque()
                q.append(cord)
                visited = set()
                if image[cord[0]][cord[1]] == 1:
                    color_check = 1
                else:
                    color_check = 0
                while q:
                
                    r,c = q.popleft()

                   
                    image[r][c] = newColor
                    dir = [1,0,-1,0,1]

                    for i in range(4):
                        new_r = r + dir[i]
                        new_c = c + dir[i+1]

                        if new_r >= 0 and new_r < m and new_c >= 0 and new_c < n and image[new_r][new_c] == color_check:
                                
                                if (new_r,new_c) not in visited:
                                    visited.add((new_r,new_c))
                                    q.append([new_r,new_c])

            bfs([sr,sc])

            return image
        
s=Solution()
print(s.floodFill([
[0, 1, 1, 0, 0, 0, 1, 1, 1],
[1, 0, 1, 0, 1, 0, 0, 0, 1],
[0, 1, 1, 0, 0, 0, 0, 1, 0],
[1, 1, 0, 1, 0, 1, 1, 1, 0],
[0, 1, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 1],
[1, 0, 1, 0, 0, 1, 1, 0, 0],
[0, 0, 1, 1, 0, 1, 0, 1, 1],
[0, 0, 0, 1, 1, 0, 1, 0, 0],
[0, 1, 1, 1, 1, 0, 1, 1, 1],],7,1,10))
# print(s.floodFill([[1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]],1,2,2))
# print(s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]],1,1,2))
# print(s.floodFill([[0, 1, 0], [0, 1, 0]],0,1,0))
                                 