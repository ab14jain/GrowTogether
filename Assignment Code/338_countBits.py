class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0]*(n+1)
        for i in range(n+1):
            bit_count = 0
            bin_arr = bin(i)[2:]

            for j in bin_arr:
                if j == '1':
                    bit_count += 1
            
            result[i] = bit_count

        return result 

# Driver code
s = Solution()
print(s.countBits(2)) # [0,1,1]
print(s.countBits(5)) # [0,1,1,2,1,2]
print(s.countBits(10)) # [0,1,1,2,1,2,2,3,1,2,2]
print(s.countBits(15)) # [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4]