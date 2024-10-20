class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        list = {}
        for i in range(1, 27):
            char = chr(i + 64)
            list[i] = char
        
        

        res = []
        while columnNumber > 0:
            remainder = columnNumber % 26
            if remainder == 0:
                remainder = 26
                columnNumber -= 1
            res.append(list[remainder])
            columnNumber = columnNumber // 26
        
        return "".join(res[::-1])
    

s = Solution()
print(s.convertToTitle(209))
# print(s.convertToTitle(750))
# print(s.convertToTitle(751))
# print(s.convertToTitle(752))
