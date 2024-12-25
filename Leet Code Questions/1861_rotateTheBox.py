class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        m = len(box)
        n = len(box[0])

        result = [['']*m for _ in range(n)] # Transpose of the box
        #Transpose the box

        for i in range(n):
            for j in range(m):
                result[i][j] = box[j][i]

        #reverse row
        for i in range(n):
            result[i].reverse()
        

        for j in range(m):
            for i in range(n-1,-1,-1):
                if result[i][j] == '.':
                    row = -1
                    for k in range(i-1,-1,-1):
                        if result[k][j] == '*':                            
                            break

                        if result[k][j] == '#':
                            row = k
                            break
                    
                    if row != -1:
                        result[row][j] = '.'
                        result[i][j] = '#'


        return result


s=Solution()
print(s.rotateTheBox([["#",".","#"]])) # [["."],["."],["#"]]
print(s.rotateTheBox([["#",".","*","."],["#","#","*","."],["#","#",".","."]])) # [[".","#","#"],[".","#","#"],["#","*","."],[".","."]]