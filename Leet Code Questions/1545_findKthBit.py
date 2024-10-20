import math


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        if n == 1:
            return '0'
        
        binary_len = (1 << n) - 1

        if k < math.floor(binary_len/2):
            return self.findKthBit(n-1, k)
        elif k == math.floor(binary_len/2):
            return '1'
        else:
            ch = self.findKthBit(n-1, (binary_len - k - 1))
            if ch == '0': 
                return '1'
            else:
                return '0'

s = Solution()
# print(s.findKthBit(3, 1)) # 0
print(s.findKthBit(4, 11)) # 1
# print(s.findKthBit(1, 1)) # 0
# print(s.findKthBit(2, 3)) # 1