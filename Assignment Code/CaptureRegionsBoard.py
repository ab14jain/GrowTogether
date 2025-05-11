class Solution:
    # @param A : list of list of chars
    def solve(self, A):

        m = len(A)
        n = len(A[0])
        boundry_o = []
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1) or (j == 0 or j == n-1):
                    if A[i][j] == 'O':
                        boundry_o.append([i,j])
        
        
        while boundry_o:
            x,y = boundry_o.pop()
            A[x][y] = 'NA'

            dir = [1,0,-1,0,1]

            for i in range(4):
                new_x = x + dir[i]
                new_y = y + dir[i+1]

                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                    if A[new_x][new_y] == 'O':
                        boundry_o.append([new_x,new_y])

        for i in range(m):
            for j in range(n): 
                if A[i][j] == 'NA':
                    A[i][j] = 'O'
                else:
                    A[i][j] = 'X'
        return A
    
s=Solution()
print(s.solve([['X', 'X','X', 'X'],['X', 'O','O', 'X'],['X', 'X','O', 'X'],['X', 'O','X', 'X']]))

print(s.solve([
       ['X', 'O', 'O'],
       ['X', 'O', 'X'],
       ['O', 'O', 'O']
     ]))
print(s.solve([
       ['X', 'O', 'X'],
       ['X', 'O', 'X'],
       ['X', 'O', 'X']
     ]))