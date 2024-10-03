class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        count = 0
        i = 1
        while(i*i <= A):
            if A%i == 0:
                if i == A/i:
                    count += 1
                else:
                    count += 2            
            
            i += 1
        
        return count
    

s= Solution()
print(s.solve(6)) # 4