class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):

        # Print spiral matrix
        result = [[0]*A for i in range(A)]
        top = 0
        bottom = A - 1
        left = 0
        right = A - 1
        count = 1

        while top <= bottom and left <= right:
            for i in range(left, right+1):
                result[top][i] = count
                count += 1
            top += 1

            for i in range(top, bottom+1):
                result[i][right] = count
                count += 1
            right -= 1

            for i in range(right, left-1, -1):
                result[bottom][i] = count
                count += 1
            bottom -= 1

            for i in range(bottom, top-1, -1):
                result[i][left] = count
                count += 1
            left += 1
        
        return result
    

        # result = [[0]*A]*A
        # while A > 1:
        #     i = 0
        #     j = 0
        #     count = 1
        #     temp = result[0][:]
        #     for k in range(1, A):
        #         temp[j] = count
        #         count += 1
        #         j += 1
            
        #     result[0] = temp[:]
            
        #     temp = result[:][A-1]
        #     for k in range(1, A):
        #         temp[i] = count
        #         count += 1
        #         i += 1
            
        #     result[:][A-1] = temp[:]
            
        #     for k in range(1, A):
        #         temp[i][j] = count
        #         count += 1
        #         j -= 1
            
        #     result = temp[:]
            
        #     for k in range(1, A):
        #         temp[i][j] = count
        #         count += 1
        #         i -= 1           

        #     result = temp[:]
        #     A -= 2
        #     i += 1
        #     j += 1
        
        # if A == 1:
        #     result[i][j] = count
        
        # return result
    

s = Solution()
print(s.generateMatrix(3)) # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
print(s.generateMatrix(4)) # [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
print(s.generateMatrix(5))