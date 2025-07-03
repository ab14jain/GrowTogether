class Solution:
    def kthCharacter(self, k: int) -> str:
        
        s = 'a'
        idx = k
        while len(s) < idx:

            t = len(s)
            i = 0
            nxt = ''
            while i < t:
                
                if (ord(s[i]) + 1) <= 122:
                    nxt += chr((ord(s[i]) + 1))
                else:
                    nxt += (ord(s[i]) + 1 - 122)
                i += 1
            s += nxt
            k -= 1

        return s[idx-1]

s=Solution()
print(s.kthCharacter(2))
print(s.kthCharacter(5))