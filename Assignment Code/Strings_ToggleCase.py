class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        res = []
        for i in range(len(A)):
            ascii_val = ord(A[i])
            if (ascii_val >= 97 and ascii_val <= 122):
                res.append(chr(ascii_val - 32))            
            else:
                res.append(chr(ascii_val + 32))
            
        
        return ("").join(res)
    

s = Solution()
A = "abCD"
print(s.solve(A)) # ABcd

