# https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1

class Solution:
    def spirallyTraverse(self, mat):
        # code here
        result = []
        m = len(mat)
        n = len(mat[0])

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1

            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1
            
        return result

s=Solution()
print(s.spirallyTraverse([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(s.spirallyTraverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])) # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
print(s.spirallyTraverse([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]])) # [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7]
print(s.spirallyTraverse([[32, 44, 27, 23], [54, 28, 50, 62]])) # [32, 44, 27, 23, 62, 50, 28, 54]
