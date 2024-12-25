class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
    	# code here 
    	
        m = len(mat)
        n = len(mat[0])
        i = 0
        j = n-1

        while i < m:
            if mat[i][j] == x:
               return True
            elif mat[i][j] < x:
               i += 1
            else:
                low = 0
                high = n-1
                while low <= high:
                    mid = (low + high) // 2
                    if mat[i][mid] == x:
                        return True
                    elif mat[i][mid] < x:
                        low = mid + 1
                    else:
                        high = mid - 1
                i += 1
        return False
    
s=Solution()
mat = [[3,4,8], [2, 5, 6], [9, 25, 27]]
print(s.searchRowMatrix(mat, 9)) # True
# mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(s.searchRowMatrix(mat, 8)) # True
# mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# print(s.searchRowMatrix(mat, 15)) # False
# print(s.searchRowMatrix(mat, 35)) # False

