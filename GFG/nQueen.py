#https://www.geeksforgeeks.org/problems/n-queen-problem0315/1

class Solution:
    def nQueenPlacements(self, j, n, board, rows, diag1, diag2, res):
        if j > n:       
            res.append(board[:])
            return

        for i in range(1, n + 1):
            if not rows[i] and not diag1[i + j] and not diag2[i - j + n]:            
                rows[i] = diag1[i + j] = diag2[i - j + n] = True
                board.append(i)            
                self.nQueenPlacements(j + 1, n, board, rows, diag1, diag2, res)
                board.pop()
                rows[i] = diag1[i + j] = diag2[i - j + n] = False

    def nQueen(self, n):
        ans = []
        board = []    
        rows = [False] * (n + 1)   
        diag1 = [False] * (2 * n + 1)
        diag2 = [False] * (2 * n + 1)
        
        self.nQueenPlacements(1, n, board, rows, diag1, diag2, ans)
        return ans
    

s=Solution()
print(s.nQueen(2))
print(s.nQueen(4))
print(s.nQueen(1))
print(s.nQueen(8))