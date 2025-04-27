from collections import deque


class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @param D : integer
	# @param E : list of integers
	# @param F : list of integers
	# @return a strings
	def solve(self, A, B, C, D, E, F):

		# def is_within_circle(x, y, cx, cy, r):
		# 	return (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2

		# # self.R = D
		# q = deque()
		# q.append((0,0))
		# visited = [[False]*(B+1) for _ in range(A+1)]
		# directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
		# for i in range(C):
		# 	cx,cy = E[i],F[i]
		# if (cx==A and cy==B) or (cx==0 and cy==0):
		# 	return 'NO'
		# visited[cx][cy] = True
		# for x in range(max(0,cx-D), min(A,cx+D)+1):
		# 	for y in range(max(0, cy-D), min(B,cy+D)+1):
		# 		if is_within_circle(x,y,cx,cy,D):
		# 			visited[x][y] = True
		# while q:

		# 	r,c = q.popleft()
		# 	if r==A and c==B:
		# 		return 'YES'
		# 	for x,y in directions:
		# 		nx = r+x
		# 		ny = c+y

		# 		if nx==A and ny==B:
		# 			return 'YES'

		# 		if 0<=nx<=A and 0<=ny<=B and not visited[nx][ny]:
		# 			visited[nx][ny] = True
		# 			q.append((nx,ny))
		# 	return 'NO'

		circlePoints = []

		for i in range(C):
			x = E[i]
			y = F[i]
			circlePoints.append([x,y])
			for r in range(1, D+1):			
				if x+r <= A:
					circlePoints.append([x+r,y])
				
				if x-r >= 0:
					circlePoints.append([x-r,y])

				if y+r <= B:	
					circlePoints.append([x,y+r])
				if y-r >= 0:
					circlePoints.append([x,y-r])

		
		
		def bfs(cord):

			q = deque()
			q.append(cord)
			visited = []

			while q:
				x,y = q.popleft()

				if x == A and y == B:
					return "YES"
				
				visited.append([x,y])
				directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

				for i in range(8):
					new_x = x + directions[i][0]
					new_y = y + directions[i][1]

					if new_x >= 0 and new_x <= A and new_y >= 0 and new_y <= B and [new_x,new_y] not in circlePoints:
						
						if new_x == A and new_y == B:
							return "YES"
						
						if [new_x,new_y] not in visited:	
							q.append([new_x,new_y])
				
			return "NO"
		
		if [A,B] in circlePoints:
			return "NO"
            
		if [0,0] in circlePoints:
			return "NO"
			
		return bfs([0,0])
			
s=Solution()
print(s.solve(41,67,5,0,[17,16,12,0,40],[52,61,61,25,31]))
print(s.solve(1,1,1,1,[0],[0]))
print(s.solve(2,3,1,1,[2],[3]))
print(s.solve(3,3,1,1,[0],[3]))
print(s.solve(4,4,3,1,[1,0,3],[3,2,1]))