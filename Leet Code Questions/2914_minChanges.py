class Solution:
    def minChanges(self, s: str) -> int:
        
        char = s[0]
        count = 0
        change = 0

        for i in range(len(s)):
            if s[i] == char:
                count += 1
            else:
                if count % 2 == 0:
                    count = 1
                else:
                    change += 1
                    count = 0
            char = s[i]
        return change


s= Solution()
print(s.minChanges("1010")) # 1
print(s.minChanges("1111")) # 1
print(s.minChanges("1110")) # 1
print(s.minChanges("10")) # 1
print(s.minChanges("1011")) # 1
print(s.minChanges("100010000011")) # 1
print(s.minChanges("100010000111")) # 1