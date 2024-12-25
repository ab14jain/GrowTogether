class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        print(2**26)

        #Approach 1 - Recursion
        def powerThree(n):
            if n ==  0:
                return False
            if n == 1:
                return True
            
            if n % 3 == 0: return powerThree(n//3)
            return False

        return powerThree(n)

        #Approach 2 - Iterative
        # if n <= 0:
        #     return False
        # rem = 0
        # while n > 0:
        #     if n < 3:
        #         if n == 1 and rem == 0:
        #             return True
        #         else:
        #             return False
        #     rem = n % 3
        #     if rem != 0:
        #         return False
        #     n = n // 3     
            


s= Solution()
print(s.isPowerOfThree(19683)) # True
print(s.isPowerOfThree(0)) # False
print(s.isPowerOfThree(9)) # True
print(s.isPowerOfThree(45)) # False
print(s.isPowerOfThree(1)) # True