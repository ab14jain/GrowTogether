class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # while n > 0:
        #     if(n % 2 == 1):
        #         count += 1
            
        #     n = n // 2

        bit_arr = bin(n)

        for i in bit_arr:
            if i == '1':
                count += 1
        
        return count

s = Solution()
print(s.hammingWeight(11))
print(s.hammingWeight(128))
print(s.hammingWeight(4294967293))
print(s.hammingWeight(0))