from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Time Complexity: O(m × n) — you traverse the matrix twice.

        # Space Complexity: O(m + n) — for the two sets.

        # zeros_row = set()
        # zeros_coll = set()
        # m = len(matrix)
        # n = len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             zeros_row.add(i)
        #             zeros_coll.add(j)

        # for i in range(m):
        #     for j in range(n):
        #         if i in zeros_row or j in zeros_coll:
        #             matrix[i][j] = 0
        
        # return matrix
        
        # Time Complexity	O(m × n)
        # Space Complexity	O(1)
        m = len(matrix)
        n = len(matrix[0])

        isfirstrowhaszero = False
        isfirstcollhaszero = False

        for i in range(n):            
            if matrix[0][i] == 0:
                isfirstrowhaszero = True

        for i in range(m):            
            if matrix[i][0] == 0:
                isfirstcollhaszero = True

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        
        for i in range(1, m):            
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if isfirstrowhaszero:
            for i in range(n):            
                matrix[0][i] = 0

        if isfirstcollhaszero:
            for i in range(m):            
                matrix[i][0] = 0
        
        return matrix

s=Solution()
print(s.setZeroes([[1,0,3]]))
print(s.setZeroes([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]))
print(s.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
