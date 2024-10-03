class Solution:
    def isHappy(self, n: int) -> bool:

        if n == 1:
            return 1
        
        square_sum = []
        temp_square_sum = 0
        while n > 0:
            temp_square_sum += (n % 10) ** 2
            n = n // 10
            if n == 0:
                if temp_square_sum == 1:
                    return 1
                elif temp_square_sum in square_sum:
                    return 0
                else:
                    square_sum.append(temp_square_sum)
                    n = temp_square_sum
                    temp_square_sum = 0


# Test cases
s = Solution()
print(s.isHappy(2342342342342342342342342342342342342342342342342342))  # True