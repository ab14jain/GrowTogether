class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        
        maxNum = 2**maximumBit - 1
        res = []
        xor = 0
        for num in nums:
            xor ^= num
            res.append(maxNum ^ xor)
        res.reverse()
        return res
    

s= Solution()
print(s.getMaximumXor([0,1,2,3,4], 3)) # [7, 6, 5, 4, 3]
print(s.getMaximumXor([2,3,4,7], 3)) # [5, 4, 3, 0]
print(s.getMaximumXor([0,1,2,3,4], 1)) # [0, 1, 3, 2, 1]
print(s.getMaximumXor([0,1,2,3,4], 2)) # [3, 2, 1, 0, 3]
print(s.getMaximumXor([0,1,2,3,4], 3)) # [7, 6, 5, 4, 3]
print(s.getMaximumXor([0,1,2,3,4], 4)) # [15, 14, 13, 12, 11]