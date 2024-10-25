class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_arr = list(s)
        n = len(s)
        max_palindrome = []
        final_l = 0
        final_r = 0
        max_len = 0
        for i in range(n):
            c = i
            l = c
            r = c
            while l > -1 and r < n:                
                if str_arr[l] != str_arr[r]:
                    break

                l -= 1
                r += 1

            if(max_len < r - l - 1):
                max_len = r - l - 1
                final_l = l
                final_r = r

            c = i
            l = c
            r = c + 1
            while l > -1 and r < n :                
                if str_arr[l] != str_arr[r]:
                    break

                l -= 1
                r += 1
            
            if(max_len < r - l - 1):
                max_len = r - l - 1
                final_l = l
                final_r = r

        for k in range(final_l + 1, final_r):
            max_palindrome.append(str_arr[k])

        return "".join(max_palindrome)
    
# Time complexity: O(n^2)
# Space complexity: O(n)
s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("a"))
print(s.longestPalindrome("ac"))
print(s.longestPalindrome("bb"))