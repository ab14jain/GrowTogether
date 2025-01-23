from collections import defaultdict


class Solution:
    def numWays(self, words: list[str], target: str) -> int:

        # mod = 10**9 + 7
        # count = defaultdict(int)

        # for word in words:
        #     for i, c in enumerate(word):
        #         count[(i,c)] += 1


        # dp = {}

        # def dfs(i, k):
        #     if i == len(target):
        #         return 1
            
        #     if k == len(words[0]):
        #         return 0
            
        #     if (i, k) in dp:
        #         return dp[(i, k)]
            
        #     curr_char = target[i]
        #     dp[(i, k)] =  dfs(i, k + 1)
        #     dp[(i, k)] += count[(k,curr_char)] * dfs(i + 1, k + 1)
            
        #     return dp[(i, k)] % mod
        
        # return dfs(0, 0)    


        k = len(words[0])
        m = len(target)
        mod = 10**9 + 7
        # freq = [[0] * 26 for _ in range(k)]

        # for i in range(k):
        #     for word in words:            
        #         freq[ord(word[i]) - ord('a')][i] += 1

        # Initialize a 2D list to store frequencies
        freq = [[0 for _ in range(k)] for _ in range(26)]

        # Iterate through each column
        for col in range(k):
            for word in words:
                # Update the frequency for the current character in the current column
                freq[ord(word[col]) - ord('a')][col] += 1

       
        
        dp = [[0] * (k + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for i in range(m + 1):
            for j in range(k + 1):
                if j < k:
                    dp[i][j+1] = (dp[i][j+1] + dp[i][j]) % mod 
                if i < m and j < k:
                    dp[i+1][j+1] = (dp[i+1][j+1] + dp[i][j] * freq[ord(target[i]) - ord('a')][j]) % mod

        return dp[m][k]

s=Solution()
print(s.numWays(["a"],"z"))
print(s.numWays(["daa","ccd","bdc"],"ab"))
print(s.numWays(["acca","bbbb","caca"],"aba"))
print(s.numWays(["abba","baab"],"ab"))