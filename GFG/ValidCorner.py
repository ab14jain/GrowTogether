#https://www.geeksforgeeks.org/problems/find-rectangle-with-corners-as-1--141631/1

class Solution:    
    def ValidCorner(self,mat): 
        # Code here 

        

        # Approach 1 - Brute Force
        # The idea is to check all possible submatrices of size at least 2 × 2 by iterating through every pair of rows and every pair of columns. 
        # For each such combination (quadruple), we verify if the four corners of the submatrix are all 1s. 
        # If such a rectangle is found, we return true immediately. This approach ensures that we don't miss any valid configuration.
        
        # m = len(mat)
        # n = len(mat[0])
        # for i in range(m):
        #     for j in range(n):

        #         for x in range(1, m-i):
        #             for y in range(1, n-j):
        #                 if mat[i][j] == 1 and mat[i+x][j] == 1 and mat[i][j+y] == 1 and mat[i+x][j+y] == 1:
        #                     return True
        
        # return False


        row = len(mat)
        coll = len(mat[0])

        seen = set()

        for r in range(row):

            for c1 in range(coll-1):
                for c2 in range(c1+1, coll):

                    if mat[r][c1] == 1 and mat[r][c2] == 1:

                        pair = str(c1) + "," + str(c2)
                        if pair in seen:
                            return True
                        
                        seen.add(pair)

        return False

s=Solution()
print(s.ValidCorner([
        [1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1]
    ]))

        # def recur(grid, i, j, x, y):

        #     if x > n or y > m:
        #         return
            
        #     if grid[i][j]:
        #         return True
            

        #     for k in range(m-i):
        #         for l in range(n-j):

        #             recur(grid, i+1, j, x+1, y)
        #             recur(grid, i, j+1, x, y+1)

        # for i in range(m):
        #     for j in range(n):

        #         if recur(mat, i, j):
        #             return True
                
        # return False