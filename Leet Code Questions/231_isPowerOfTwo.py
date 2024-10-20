class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 0:
            return False
            
        while n > 0:
            if n == 1:
                return True

            if n % 2 == 1:
                return False
            n = n // 2


s = Solution()
print(s.isPowerOfTwo(1))
print(s.isPowerOfTwo(16))
print(s.isPowerOfTwo(218))
print(s.isPowerOfTwo(0))
print(s.isPowerOfTwo(3))