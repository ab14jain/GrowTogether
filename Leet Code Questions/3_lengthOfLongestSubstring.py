class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        # if n == 2:
        #     if s[0] == s[1]:
        #         return 1
        #     else:
        #         return 2
            
        
        i = 0
        j = 0
        max_len = 0
        char_dict = {}
        while j < n:
            if s[j] not in char_dict:
                char_dict[s[j]] = 1
            else:
                while s[i] != s[j]:
                    del char_dict[s[i]]
                    i += 1
                
                i += 1                
                char_dict[s[j]] = 1
            
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len
    

# Time complexity: O(n)
# Space complexity: O(n)

s=Solution()
print(s.lengthOfLongestSubstring("abcabcbb")) # 3
print(s.lengthOfLongestSubstring("bbbbb")) # 1
print(s.lengthOfLongestSubstring("pwwkew")) # 3
print(s.lengthOfLongestSubstring(" ")) # 1
print(s.lengthOfLongestSubstring("au")) # 2
                