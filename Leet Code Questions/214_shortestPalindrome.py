class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        lps = [0] * n
        org_str = s
        def computeLPS(pat):
            n = len(pat)
            lps = [0] * n
            length = 0
            i = 1
            while i < n:           
                
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        n = len(s)
        rev = s[::-1]        
        s = s + "$" + rev        
        lps = computeLPS(s)  
        char_count = n - lps[-1]
        if char_count == 0:
            return org_str
        last_char = org_str[-char_count:]    
        reversed_last_char = last_char[::-1]
        final_str = reversed_last_char + org_str
        return final_str

s=Solution()
print(s.shortestPalindrome("aacecaaa"))
print(s.shortestPalindrome("abcd"))
print(s.shortestPalindrome("a"))
print(s.shortestPalindrome("aabaa"))