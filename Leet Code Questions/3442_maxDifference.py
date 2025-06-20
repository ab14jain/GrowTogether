from typing import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        n = len(s)
        minE = n+1
        maxO = 1

        for ch in counter:
            if counter[ch] % 2 == 0:
                minE = min(minE, counter[ch])
            else:
                maxO = max(maxO, counter[ch])

        return maxO - minE