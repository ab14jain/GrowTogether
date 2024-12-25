from typing import Counter


class Solution:
    def similarPairs(self, words: list[str]) -> int:

        n = len(words)
        similar_pairs = 0
        for i in range(n):
            for j in range(i+1, n):
                if self.isSimilar(words[i], words[j]):
                    similar_pairs += 1

        return similar_pairs
    

    def isSimilar(self, word1: str, word2: str) -> bool:
        count_1 = Counter(word1)
        count_2 = Counter(word2)
        if count_1.keys() == count_2.keys():
            return True
        else:
            return False        

s= Solution()
print(s.similarPairs(["abc", "abc", "abc"])) # 3
print(s.similarPairs(["abc", "abc", "ab"])) # 2
print(s.similarPairs(["abc", "abc", "ab", "abc"])) # 4
print(s.similarPairs(["abc", "abc", "ab", "abc", "abc"])) # 5
print(s.similarPairs(["abc", "abc", "ab", "abc", "abc", "abc"])) # 6
        