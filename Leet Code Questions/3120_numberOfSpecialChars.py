class Solution:
    def numberOfSpecialChars(self, word: str) -> int:        
        chars_map = {}
        for c in word:
            chars_map[ord(c)] = c

        seen = set()
        count = 0
        for c in word:
            if (ord(c) + 32) in chars_map and c not in seen:
                seen.add(c)
                count += 1
        
        return count
    
s = Solution()
print(s.numberOfSpecialChars('aaAbcBC')) # 3
# print(s.numberOfSpecialChars('USA')) # 3
# print(s.numberOfSpecialChars('leetcode')) # 8