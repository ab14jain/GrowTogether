#https://www.geeksforgeeks.org/problems/word-search/1

class Solution:
	def isWordExist(self, mat, word):
		#Code here
            m = len(mat)
            n = len(mat[0])
            visited = [[False]*n for _ in range(m)]

            def is_valid(r, c):
                return r >= 0 and r < m and c >= 0 and c < n

            def find_word(mat, r, c, visited, wlength):   
                
                if len(word) == wlength:
                    return True
                
                if is_valid(r,c) and mat[r][c] != word[wlength]:
                    return False

                if is_valid(r,c) and not visited[r][c]:
                    visited[r][c] = True

                    if find_word(mat, r+1, c, visited, wlength+1):
                        return True
                    if find_word(mat, r-1, c, visited, wlength+1):
                        return True
                    if find_word(mat, r, c+1, visited, wlength+1):
                        return True
                    if find_word(mat, r, c-1, visited, wlength+1):
                        return True

                    visited[r][c] = False

            for i in range(m):
                for j in range(n):
                    if mat[i][j] == word[0] and find_word(mat, i, j, visited, 0):
                        return True
            
            return False


s=Solution()
print(s.isWordExist([['T', 'E', 'E'], ['S', 'G', 'K'], ['T', 'E', 'L']], "GEEK"))
print(s.isWordExist([['T', 'E', 'U'], ['S', 'G', 'K'], ['T', 'E', 'L']], "GEEK"))
print(s.isWordExist([['A', 'B', 'A'], ['B', 'A', 'B']], "AB"))
print(s.isWordExist([['A', 'B', 'A'], ['B', 'A', 'B']], "ABC"))