import math


class Solution:
    def boundarySum(self, n : int, matrix : list[list[int]]) -> list[int]:
        # code here
        res = []        
        
        noofboundary = math.ceil(n/2)
        boundry = 0

        while boundry < noofboundary:
            sum = 0
            mat = []
            for i in range(boundry, n - boundry):
                if i == 0 + boundry or i == n - 1 - boundry:
                    for j in range(boundry, n - boundry):
                        sum += matrix[i][j]   
                
                if i > boundry and i < n - 1 - boundry:
                    sum += matrix[i][boundry]
                    sum += matrix[i][n - 1 - boundry]                             
            
            
            res.append(sum)
            boundry += 1

        return res
    
s = Solution()

# print(s.boundarySum(3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # [1, 5, 7, 9, 17, 3]
print(s.boundarySum(4, [[1, 2, 3, 4], [2, 3, 4, 5], [4, 1, 5, 2], [3, 2, 9, 0]])) # [1, 5, 9, 13, 14, 15, 16, 12, 8, 4]
#print(s.boundarySum(5, [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [4, 1, 5, 2, 7], [3, 2, 9, 0, 5], [7, 1, 3, 6, 2]]))
           