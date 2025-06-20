from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        nums = []

        for i in range(1, n+1):
            nums.append(str(i))

        nums.sort()
        ans = list(map(int, nums))
        return ans

s=Solution()
print(s.lexicalOrder(13))