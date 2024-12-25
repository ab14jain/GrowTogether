class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        
        min_num = float('inf')
        negative_count = 0
        total_sum = 0
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                total_sum += abs(matrix[r][c])
                min_num = min(min_num,abs(matrix[r][c]))
                if matrix[r][c] < 0:
                    negative_count += 1
                
        
        if negative_count % 2 == 0:
            return total_sum
        else:
            return (total_sum - 2*min_num)

s=Solution()
print(s.maxMatrixSum([[-1,-2,-3],[-2,-3,-3],[-3,-3,-3]])) # -21
print(s.maxMatrixSum([[1,2,3],[2,3,3],[3,3,3]])) # 23
print(s.maxMatrixSum([[1,2,3],[-2,-3,-3],[3,3,3]])) # 21
print(s.maxMatrixSum([[1,2,3],[2,3,3],[3,3,3]])) # 23
print(s.maxMatrixSum([[1,2,3],[2,3,3],[3,3,3]])) # 23