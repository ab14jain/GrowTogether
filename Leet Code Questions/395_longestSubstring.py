class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        #not solved
        n = len(s)
        i = 0
        j = 0

        max_unique_length = 0

        char_map = {}

        while j < n:
            if s[j] not in char_map:
                char_map[s[j]] = 0
            char_map[s[j]] += 1

            while i <= j and min(char_map.values()) >= k:
                max_unique_length = max(max_unique_length, j - i + 1)

                char_map[s[i]] -= 1

                if char_map[s[i]] == 0:
                    del char_map[s[i]]

                i += 1

            j += 1
        
        return max_unique_length
    
# Time complexity: O(n)
# Space complexity: O(1)

s=Solution()
print(s.longestSubstring("aaabb", 3)) # 3
print(s.longestSubstring("abaccc", 3)) # 0
print(s.longestSubstring("abcabc", 3)) # 0
print(s.longestSubstring("aaabb", 2)) # 2
print(s.longestSubstring("aaabb", 1)) # 1
