class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        def calc_LPS(pref, n, lps):
            i = 0
            j = 1

            while(j<n):
                if pref[i] == pref[j]:
                    lps[j] = 1 + i
                    i += 1
                    j += 1
                else:
                    if i > 0:
                        i = lps[i-1]
                    else:
                        j += 1

        def clear_substr(s, pref, lps):
            m = len(s)
            n = len(pref)
            i = 0
            j = 0

            while(i < m):
                if s[i] == pref[j]:
                    i += 1
                    j += 1
                
                if j == n:
                    s = s[:i-n]+s[i:]
                    m = len(s)
                    i = max(0, i-2*n)
                    j = 0

                if i < m and s[i] != pref[j]:
                    if j == 0:
                        i += 1
                    else:
                        j = lps[j-1]

            return s
    
        n = len(part)
        lps = [0]*n

        calc_LPS(part,n,lps)
        return clear_substr(s,part,lps)
        
    
s=Solution()

print(s.removeOccurrences("daabcbaabcbc","abc"))
print(s.removeOccurrences("axxxxyyyyb","xy"))