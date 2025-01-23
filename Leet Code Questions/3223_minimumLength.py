class Solution:
    def minimumLength(self, s: str) -> int:

        n = len(s)
        char_map = [0] * 26
        count = 0

        for i in range(n):
            char_map[ord(s[i]) - ord('a')] += 1

        for i in range(26):
            if char_map[i] & 1:
                count += 1
            else:
                count += min(2, char_map[i])
            
        return count
    

s=Solution()
print(s.minimumLength("abaacbcbb")) # 3
print(s.minimumLength("ababa")) # 1