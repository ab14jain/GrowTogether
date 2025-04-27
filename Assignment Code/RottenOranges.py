#https://www.scaler.com/academy/mentee-dashboard/core-curriculum/m/4/classes

from collections import deque


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        twos = deque()
        ones = 0
        m = len(A)
        n = len(A[0])

        def isvalid(x,y):
            return x >= 0 and x < m and y >= 0 and y < n

        for i in range(m):
            for j in range(n):
                if A[i][j] == 2:
                    twos.append([i,j,0])
                    A[i][j] = 3
                if A[i][j] == 1:
                    ones += 1 

        if ones == 0:
            return 0
        
        ans = 0
        while twos:
            i,j,t = twos.popleft()
            
            ans = t
            dir = [1,0,-1,0,1]
            for k in range(4):
                x = i + dir[k]
                y = j + dir[k+1]
                if isvalid(x,y):                    
                    if A[x][y] == 1:
                        twos.append([x,y,t+1])
                        A[x][y] += 1
                        ones -= 1
        
        if ones == 0:
            return ans

        return -1
    
s=Solution()
print(s.solve([[2, 1, 1],[1, 1, 0],[0, 1, 1]]))
print(s.solve([[2, 1, 1],[0, 1, 1],[1, 0, 1]]))