# https://www.geeksforgeeks.org/problems/solve-the-sudoku-1587115621/1

class Solution:

    def is_valid(self, i, j, num, row, col, box):
        if (row[i] & (1 << num)) or (col[j] & (1 << num)) or (box[i // 3 * 3 + j // 3] & (1 << num)):
            return False
        return True

    def solve_sudoku(self, mat, i, j, row, col, box):
        n = len(mat)        
        if i == n - 1 and j == n:
            return True
                
        if j == n:
            i += 1
            j = 0
        
        if mat[i][j] != 0:
            return self.solve_sudoku(mat, i, j + 1, row, col, box)

        for num in range(1, n + 1):
            
            if self.is_valid(i, j, num, row, col, box):
                mat[i][j] = num
                
                row[i] |= (1 << num)
                col[j] |= (1 << num)
                box[i // 3 * 3 + j // 3] |= (1 << num)

                if self.solve_sudoku(mat, i, j + 1, row, col, box):
                    return True
                
                mat[i][j] = 0
                row[i] &= ~(1 << num)
                col[j] &= ~(1 << num)
                box[i // 3 * 3 + j // 3] &= ~(1 << num)

        return False
    
    
    def solveSudoku(self, mat):
        
        # Your code here

        n = len(mat)
        row = [0] * n
        col = [0] * n
        box = [0] * n
        
        for i in range(n):
            for j in range(n):
                if mat[i][j] != 0:
                    row[i] |= (1 << mat[i][j])
                    col[j] |= (1 << mat[i][j])
                    box[(i // 3) * 3 + j // 3] |= (1 << mat[i][j])

        self.solve_sudoku(mat, 0, 0, row, col, box)

        return mat


mat = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]
s=Solution()
print(s.solveSudoku(mat))