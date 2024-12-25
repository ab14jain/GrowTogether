class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count = 0
        while A > 0:
            bin_rep = list(bin(A)[2:])
            if(bin_rep[-1] == '1'):
                count += 1
                
            A = A >> 1

        return count
    

# Driver code
s = Solution()
print(s.numSetBits(11)) # 3
print(s.numSetBits(0)) # 0
print(s.numSetBits(145645645)) # 1
print(s.numSetBits(245645645)) # 1
print(s.numSetBits(365464)) # 2
print(s.numSetBits(4666)) # 1
print(s.numSetBits(566666666)) # 2