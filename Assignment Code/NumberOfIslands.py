#https://www.scaler.com/academy/mentee-dashboard/class/325374/assignment/problems/4702?navref=cl_tt_nv

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        m = len(A)
        n = len(A[0])

        def dfs(grid, i,j):

            stack = []
            stack.append([i,j])
            grid[i][j] += 1
            while stack:
                x,y = stack.pop()
                dRow = [-1, 1, 0, 0, -1, -1, 1, 1]
                dCol = [0, 0, -1, 1, -1, 1, -1, 1]

                for i in range(8):
                    new_x = x + dRow[i]
                    new_y = y + dCol[i]

                    if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                        if grid[new_x][new_y] == 1:
                            stack.append([new_x,new_y])
                            grid[new_x][new_y] += 1

        count = 0                
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    dfs(A,i,j)
                    count += 1
        
        return count
    
s=Solution()
# print(s.solve([[0, 1, 0],[0, 0, 1],[1, 0, 0]]))
print(s.solve([   
       [1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [1, 0, 0, 1, 1],
       [0, 0, 0, 0, 0],
       [1, 0, 1, 0, 1]    
     ]))