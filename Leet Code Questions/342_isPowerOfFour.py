class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        #Approach 1 - Recursion
        # def powerFour(n):
        #     if n == 0: return False
        #     if n == 1: return True

        #     if n % 4 == 0: return powerFour(n//4)
        #     return False
        
        # return powerFour(n)

        #Approach 2 - Iterative
        # if n <= 0:
        #     return False
        # while n > 1:
        #     if n % 4 != 0:
        #         return False
        #     n = n // 4 
        
        # return True

        #Approach 3 - Bit Manipulation
        # return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0

        #Approach 4 - Bit Manipulation
        if n <= 0:
            return False
        while n > 1:
            if n % 4 != 0:
                return False
            n = n >> 2
        
        return True

s= Solution()
print(s.isPowerOfFour(16)) # True
print(s.isPowerOfFour(0)) # False
print(s.isPowerOfFour(1)) # True
print(s.isPowerOfFour(4)) # True
print(s.isPowerOfFour(5)) # False
print(s.isPowerOfFour(8)) # False
print(s.isPowerOfFour(9)) # False
print(s.isPowerOfFour(45)) # False
print(s.isPowerOfFour(256)) # True
print(s.isPowerOfFour(64)) # True
print(s.isPowerOfFour(81)) # False
print(s.isPowerOfFour(256)) # True
print(s.isPowerOfFour(67108864)) # True
print(s.isPowerOfFour(14348904)) # False