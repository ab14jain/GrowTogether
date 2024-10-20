class Solution:
    def minimumSteps(self, s: str) -> int:

        black_count = 0
        swap_count = 0
        for i in s:    
            if i == '1':
                black_count += 1
            else:
                swap_count += black_count

        return swap_count

s = Solution()
print(s.minimumSteps("1101"))
print(s.minimumSteps("10"))
print(s.minimumSteps("1111"))
print(s.minimumSteps("1001"))