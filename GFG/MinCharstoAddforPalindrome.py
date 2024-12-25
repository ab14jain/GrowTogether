class Solution:
    def minChar(self, s):        
        n = len(s)
        lps = [0] * n

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
        return n - lps[-1]
    

s=Solution()

print(s.minChar("AACECAAAA")) #2
print(s.minChar("ABC")) #2
print(s.minChar("ABCD")) #3
        