class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:

        # Approach 1 - Brute Force        
        # ans = []
        # for w in words:
        #     for w2 in words:
        #         if w in w2 and w != w2:
        #             ans.append(w)
        #             break
        # return ans

        # Approach 2 - Using List Comprehension
        return [w for w in words if any(w in w2 for w2 in words if w != w2)]
    
        # Approach 3 - Using KMP Algorithm
        
        

        # Approach 4 - Using Trie Data Structure


s=Solution()
print(s.stringMatching(["mass","as","hero","superhero"])) # ["as","hero"]
print(s.stringMatching(["leetcode","et","code"])) # ["et","code"]
        