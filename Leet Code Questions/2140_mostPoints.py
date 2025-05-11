from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)
        def recur(i, dp):
            if i >= n:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            skip = recur(i+1, dp)
            solve = questions[i][0] + recur(i + questions[i][1] + 1, dp)
            dp[i] = max(solve, skip)      
            return dp[i]
        
        dp = [-1]*n
        return recur(0, dp)        
    
s=Solution()
print(s.mostPoints([[12,46],[78,19],[63,15],[79,62],[13,10]]))
print(s.mostPoints([[3,2],[4,3],[4,4],[2,5]]))
print(s.mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]]))

