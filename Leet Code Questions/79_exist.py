from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])

        def is_valid(r,c):
            return r >= 0 and r < m and c >=0 and c <n

        def word_search(mat, r, c, idx, visited):            
            
            if idx == len(word):
                return True
            
            if is_valid(r,c) and mat[r][c] != word[idx]:                
                return False

            if is_valid(r,c) and not visited[r][c]:
                visited[r][c] = True
                if word_search(mat, r+1, c, idx+1, visited):
                    return True                
                if word_search(mat, r-1, c, idx+1, visited):              
                    return True
                if word_search(mat, r, c+1, idx+1, visited):
                    return True
                if word_search(mat, r, c-1, idx+1, visited):
                    return True

                visited[r][c] = False

        visited = [[False]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and word_search(board, i, j, 0, visited):
                    return True
        
        return False

s= Solution()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "CCES"))