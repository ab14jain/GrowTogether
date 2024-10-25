class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = 0
        max_ones_index = 0
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            temp_count = 0
            for j in range(m):
                if mat[i][j] == 1:
                    temp_count += 1
          
            if temp_count > max_ones:
                max_ones = temp_count
                max_ones_index = i

        return [max_ones_index,max_ones]
        

# Time complexity: O(n*m)
# Space complexity: O(1)
s = Solution()
print(s.rowAndMaximumOnes([[0,0,0,1],[0,0,1,1],[0,1,1,1],[0,0,0,0]]))
print(s.rowAndMaximumOnes([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))
