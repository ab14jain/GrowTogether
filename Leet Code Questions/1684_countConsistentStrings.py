from typing import Counter


class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
            
            allowed = set(allowed)
            consistent_strings = 0
            for word in words:
                # if all([c in allowed for c in word]):
                #     consistent_strings += 1
                counter = Counter(word)

                
                for c in allowed:
                    if c in counter:
                        consistent_strings += 1
                
    
            return consistent_strings
    
s= Solution()
print(s.countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"])) # 7
print(s.countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc", "d"])) # 7
print(s.countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc", "d", "e"])) # 7