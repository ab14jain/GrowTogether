from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        if k == 1:
            return 0
        valid_splits = []
        n = len(weights)
        for i in range(n-1):
            valid_splits.append(weights[i]+weights[i+1])

        valid_splits.sort()

        j = k-1

        max_score = sum(valid_splits[-j:])
        min_score = sum(valid_splits[:j])
        
        return max_score-min_score