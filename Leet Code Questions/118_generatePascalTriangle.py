class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        
        if numRows == 1:
            return [1]
        if numRows == 2:
            return [1, 1]
        
        res = [[1]]
        for i in range(1, numRows):
            temp = [0]*(i+1)
            temp[0] = 1
            temp[i] = 1

            for j in range(1, i):
                temp[j] = res[i-1][j-1] + res[i-1][j]
            
            res.append(temp)          

        return res


numRows = 30
s = Solution()
print(s.generate(numRows))