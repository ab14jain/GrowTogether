class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res = []

        for i in range(len(s)):
            ascii_val = ord(s[i])
            if (ascii_val >= 65 and ascii_val <= 90) or (ascii_val >= 97 and ascii_val <= 122) or (ascii_val >= 48 and ascii_val <= 57):
                
                if ascii_val >= 65 and ascii_val <= 90:
                    ascii_val = ascii_val + 32
                    res.append(chr(ascii_val))
                else:
                    res.append(s[i])
        
        i = 0
        j = len(res) - 1

        while i < j:
            if res[i] != res[j]:
                return False
            i += 1
            j -= 1
        
        return True
        #return "".join(res) == "".join(res[::-1])


s = Solution()

print(s.isPalindrome("A man, a plan, a canal: Panama"))