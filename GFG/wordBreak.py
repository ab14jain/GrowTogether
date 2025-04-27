#https://www.geeksforgeeks.org/problems/word-break1352/1

class Solution:
    def wordBreak(self, s, dictionary):
        # code here


        # def recur(i, ans):

        #     # if ans == s:
        #     #     return True
            
        #     # if i >= len(dictionary):
        #     #     return False
            
        #     # take = recur(i+1, ans+dictionary[i])
        #     # rev_take = recur(i+1, dictionary[i]+ans)
        #     # not_take = recur(i+1, ans)

        #     # return take or rev_take or not_take

        #     if i == len(ans):
        #         return True

        #     n = len(ans)
        #     prefix = ""

        #     # Try every prefix
        #     for j in range(i, n):
        #         prefix += ans[j]

        #         if prefix in dictionary and recur(j + 1, ans):
        #             return True

        #     return False
        
        # return recur(0, s)
        def recur(i, ans, dp):
            if i >= len(ans):
                return True
            if dp[i] != -1:
                return dp[i] == 1
            possible = False
            for temp in dict:
                if len(temp) > len(ans) - i:
                    continue
                if ans[i:i+len(temp)] == temp:
                    possible |= recur(i + len(temp), ans, dict, dp)
            dp[i] = 1 if possible else 0
            return possible
        
        n = len(s)
        dp = [-1] * (n + 1)
        return recur(0, s, dp)
    
s=Solution()
print(s.wordBreak("abcd", ["ab", "bcd", "b", "a"]))
print(s.wordBreak("ilike", ["i", "like", "gfg"]))
print(s.wordBreak("hhqhq", ["iajxlo", "h", "q"]))
print(s.wordBreak("ilikegfg", ["i", "like", "man", "india", "gfg"]))
print(s.wordBreak("ilikemangoes", ["i", "like", "man", "india", "gfg"]))