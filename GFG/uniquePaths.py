#https://www.geeksforgeeks.org/problems/unique-paths-in-a-grid--170647/1

class Solution:
    def uniquePaths(self, grid):
        # code here 

        rows = len(grid)
        colls = len(grid[0])
        
        dp = [[-1]*colls for _ in range(rows)]

        if grid[0][0]:
            return 0

        def isValid(r,c):
            if r >= 0 and r < rows and c >= 0 and c < colls and grid[r][c] != 1:
                return True
            return False

        def recur(grid, r, c, ways):

            if not isValid(r,c):
                return 0
            
            if dp[r][c] != -1:
                return dp[r][c]
            
            if r == rows-1 and c == colls-1:
                #count[0] += 1
                ways += 1
                return ways
                

            moveX = recur(grid, r+1, c, ways)
            moveY = recur(grid, r, c+1, ways)

            dp[r][c] = moveX + moveY

            return dp[r][c] 

        
        return recur(grid, 0, 0, 0)


        #return count[0]
    

s=Solution()
print(s.uniquePaths([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(s.uniquePaths([[1, 0, 1]]))
