class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        n = len(s)
        max_sub = 0
        for i in range(1, n-1):

            l = i - 1
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            
            max_sub = max(max_sub, r-l-1)

            l = i - 1
            r = i

            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            
            max_sub = max(max_sub, r-l-1)
    
        return max_sub

s= Solution()
print(s.longestPalindrome("abccvvvccdd")) # 7
print(s.longestPalindrome("a")) # 1
print(s.longestPalindrome("bb")) # 2
print(s.longestPalindrome("ab")) # 1
            
