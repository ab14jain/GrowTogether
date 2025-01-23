from typing import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        counter = Counter(s)
        odd_char_count = len([_ for _, v in counter.items() if v % 2 != 0])

        return odd_char_count <= k and k <= len(s)  


sol = Solution()
print(sol.canConstruct("annabelle", 2))
print(sol.canConstruct("leetcode", 3))
print(sol.canConstruct("true", 4))


