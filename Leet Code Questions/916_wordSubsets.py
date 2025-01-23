from typing import Counter


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        
        # Approach 1: Brute Force
        # result = []
        # for word in words1:
        #     hasLetter = True
        #     counter1 = Counter(word)
        #     for word2 in words2:
        #         counter2 = Counter(word2)
        #         for c in counter2:
        #             if counter2[c] > counter1[c]:
        #                 hasLetter = False
        #                 break
            
        #     if hasLetter:
        #         result.append(word)
        
        # return result

        result = []
        freq_word2 = {}
        for word in words2:
            for c in word:
                freq_word2[c] = max(freq_word2.get(c, 0), word.count(c))

        

        for word in words1:
            counter = Counter(word)
            if all(counter[c] >= freq_word2[c] for c in freq_word2):
                result.append(word) 
            
        return result

s=Solution()
print(s.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))
print(s.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["l","e"]))
print(s.wordSubsets(["warrior", "world"], ["wr", "or", "wo"]))
