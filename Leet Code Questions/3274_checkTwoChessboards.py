class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:        
        sum1 = ord(coordinate1[0]) + int(coordinate1[1])
        sum2 = ord(coordinate2[0]) + int(coordinate2[1])
        if (sum1 % 2 == 0 and sum2 % 2 == 0) or (sum1 % 2 == 1 and sum2 % 2 == 1):
            return True
        return False


# Test
coordinate1 = "a1"
coordinate2 = "h8"
solution = Solution()
print(solution.checkTwoChessboards(coordinate1, coordinate2))  # True