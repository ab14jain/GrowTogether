class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        i = 1
        while i < (n+1):            
            ans += (n//(i*10))*i + min(max(n % (i*10) - i + 1, 0),i)            
            i *= 10
        return ans