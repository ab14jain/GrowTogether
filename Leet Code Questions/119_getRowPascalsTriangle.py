class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]        
        
        
        for i in range(1, rowIndex):
           res.append(self.getPreviousRow(res, i))

        return res
    
    def getPreviousRow(self, previousRow, sumIndex) -> list[int]:
        
        if len(previousRow) == 1:
            return [[1]]
        if len(previousRow) == 2:
            return [[1], [1, 1]]
        
        return previousRow[sumIndex]
    
        