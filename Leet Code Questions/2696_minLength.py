class Solution:
    def minLength(self, s: str) -> int:
        
        substr = ["AB", "CD"]

        while "AB" in s or "CD" in s:
            for i in range(2):
                if substr[i] in s:
                    s = s.replace(substr[i], "")               
        
        return len(s)


s = Solution()
print(s.minLength("CCCCDDDD")) # 2
# print(s.minLength("ABFCACDB")) # 2
# print(s.minLength("ACBBD")) # 2
