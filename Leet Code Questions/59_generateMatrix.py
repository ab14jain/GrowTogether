class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0]*n for i in range(n)]
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
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
    
# Time complexity: O(n^2)
# Space complexity: O(n^2)
s = Solution()
print(s.generateMatrix(3))
print(s.generateMatrix(1))
print(s.generateMatrix(4))
print(s.generateMatrix(5))