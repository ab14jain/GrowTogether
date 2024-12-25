#https://www.geeksforgeeks.org/problems/search-in-a-matrix-1587115621/1
class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
    	# code here 

        # Approach 1 - Brute Force
        # Time complexity: O(m*log(n))
        # space complexity: O(1)
            # m = len(mat)
            # n = len(mat[0])
            
            # i = 0
            # j = n - 1           
            
                    
            # while i < m and j > -1:
            #     if mat[i][j] == x:
            #         return True
                
            #     if mat[i][j] > x:
            #         low = 0
            #         high = j
            #         while low <= high:
            #             mid = (low + high)//2
            #             if mat[i][mid] == x:
            #                 return True
            #             elif mat[i][mid] > x:
            #                 high = mid - 1
            #             else:
            #                 low = mid + 1
            #         return False
            #     else:
            #         i += 1
            
            # return False

        # Approach 2 - Binary Search to find the row and then binary search to find the element
        # Time complexity: O(log(m) + log(n))
        # space complexity: O(1)

        # m = len(mat)
        # n = len(mat[0])


        # lc = 0
        # rc = m - 1
        # row = -1
        # while lc <= rc:
        #     mid = (lc + rc)//2

        #     if mat[mid][0] == x:
        #         return True
        #     elif x < mat[mid][0]:
        #         rc = mid - 1
        #     else:
        #         row = mid
        #         lc = mid + 1

        # if row < 0:
        #     return False
        
        # lr = 0
        # rr = n - 1

        # while lr <= rr:
        #     mid = (lr + rr)//2

        #     if mat[row][mid] == x:
        #         return True
        #     elif mat[row][mid] >= x:
        #         rr = mid - 1
        #     else:
        #         lr = mid + 1
    
        # return False
        # 

        #Approach 3 - Binary Search in a matrix m*n. consider the matrix as a sorted 1-D array       
        #Time complexity: O(log(m*n))
        #space complexity: O(1)

        m = len(mat)
        n = len(mat[0])

        low = 0 
        high = m*n - 1

        while low <= high:
            mid = (low + high)//2

            row = mid//n
            col = mid%n

            if mat[row][col] == x:
                return True
            elif mat[row][col] < x:
                low = mid + 1
            else:
                high = mid - 1
            
        return False
    
    

s=Solution()
# mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(s.searchMatrix(mat, 51)) # True
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(s.searchMatrix(mat, 15)) # True
# Expected output: True, True 