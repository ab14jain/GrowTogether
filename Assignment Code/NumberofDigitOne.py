class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        
        ans = 0
        i = 1
        while i < (A+1):            
            ans += (A//(i*10))*i + min(max(A % (i*10) - i + 1, 0),i)            
            i *= 10
        return ans

s=Solution()
print(s.solve(100)) 
print(s.solve(926)) 