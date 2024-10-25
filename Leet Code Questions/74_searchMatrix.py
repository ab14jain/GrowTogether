class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = m - 1
        min_val = float('Inf')
        while (j > -1 and i < n):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
                i = 0
        
        return False
    
# Time complexity: O(n+m)
# Space complexity: O(1)
s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))


