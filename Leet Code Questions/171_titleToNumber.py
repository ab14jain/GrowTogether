class Solution:
    def titleToNumber(self, columnTitle: str) -> int:        
        res = 0
        for i in columnTitle:
            res = res * 26 + ord(i) - 64
        
        return res



s = Solution()
print(s.titleToNumber("A"))
print(s.titleToNumber("AB"))
print(s.titleToNumber("ZY"))
print(s.titleToNumber("HA"))
print(s.titleToNumber("GZ"))