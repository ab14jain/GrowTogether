from typing import Counter


class Solution:

    def smallestPalindrome(self, s:str) -> str:

        alphabets = [0]*26

        for ch in s:
            alphabets[ord(ch)-ord('a')] += 1

        
        oddChIndex = -1
        hasLargeLetter = False
        for i in range(26):
            if alphabets[i]%2==1:
                oddChIndex = i
                hasLargeLetter = False

            if alphabets[i] > 0 and oddChIndex < i:
                hasLargeLetter = True
            
            

        n = len(s)
        final_str = ['']*n
        left = 0
        right = n-1

        if hasLargeLetter and alphabets[oddChIndex] > n//2:      

            for j in range(0, n, 2):
                final_str[j] = chr(oddChIndex+ord('a'))
            
            for j in range(26):
                if alphabets[j] > 0 and alphabets[j]%2==0:
                    first_half = alphabets[j]//2
                    left = 1
                    right = n-2
                    for k in range(first_half):
                        final_str[left] = chr(j+ord('a')) 
                        final_str[right] = chr(j+ord('a')) 

                        left += 2
                        right -= 2

            oddChIndex = -1

            return "".join(final_str)
        
        for i in range(26):
            if alphabets[i] > 0 and alphabets[i]%2==0:
                first_half = alphabets[i]//2

                for k in range(first_half):
                    final_str[left] = chr(i+ord('a')) 
                    final_str[right] = chr(i+ord('a')) 

                    left += 1
                    right -= 1
                      


        if oddChIndex != -1:
            for i in range(alphabets[oddChIndex]):
                final_str[left] = chr(oddChIndex+ord('a'))  
                left += 1

        return "".join(final_str)


s=Solution()
# print(s.smallestPalindrome("z"))
# print(s.smallestPalindrome("ababa"))
print(s.smallestPalindrome("babab"))
# print(s.smallestPalindrome("daccad"))
# print(s.smallestPalindrome("dbbcccaaacccbbd"))

