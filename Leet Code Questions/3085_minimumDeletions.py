from typing import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        
        counter = Counter(word)

        