class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        n = len(s)
        a = 0
        b = 0
        c = 0

        l = 0
        r = 0
        count = 0
        while r < n:   
            if s[r] == 'a':
                a += 1
            elif s[r] == 'b':
                b += 1
            elif s[r] == 'c':
                c += 1            

            while a > 0 and b > 0 and c > 0:
                count += (n-r)                
                if s[l] == 'a':
                    a -= 1
                elif s[l] == 'b':
                    b -= 1
                elif s[l] == 'c':
                    c -= 1
                l += 1    
            r += 1

        return count      
        
        

s=Solution()
print(s.numberOfSubstrings("abcabc"))
print(s.numberOfSubstrings("aaacb"))
print(s.numberOfSubstrings("abc"))
            
