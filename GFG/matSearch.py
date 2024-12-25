class Solution:
	def matSearch(self, mat, x):
		# Complete this function
		
            m = len(mat)
            n = len(mat[0])

            # Approach 1 - Brute Force
            # for i in range(m):
            #     for j in range(n):
            #         if mat[i][j] == x:
            #             return True
            
            # return False

            # Approach 2 - Optimized
     
            # [01, 02, 03, 04], 
            # [05, 06, 07, 08], searchRowMatrix
            # [09, 10, 11, 12], 
            # [13, 14, 15, 16]

            i = 0
            j = n-1

            while i < m and j >= 0:
                if mat[i][j] == x:
                    return True
                elif mat[i][j] < x:
                    i += 1
                else:
                    j -= 1
            return False
     
s=Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(s.matSearch(mat, 5)) # True
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(s.matSearch(mat, 16)) # True
