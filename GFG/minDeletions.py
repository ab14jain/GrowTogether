#https://www.geeksforgeeks.org/problems/minimum-deletitions1648/1

from typing import Counter


class Solution:
    def minDeletions(self,s):
        # code here 


        n = len(s)

        def count_min(s, i, j, dp):

            if i > j:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] == s[j]:
                return count_min(s, i+1, j-1, dp)
            
            calc = 1 + min(count_min(s, i+1, j, dp), count_min(s, i, j-1, dp))
            dp[i][j] = calc
            return dp[i][j]

        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return count_min(s, 0, n-1, dp)
        # def isPalindrome(s):

        #     n = len(s)
        #     i = 0
        #     j = n-1
        #     while i < j:
        #         if s[i] != s[j]:
        #             return False
                
        #         i += 1
        #         j -= 1
            
        #     return True
        

        # # n = len(s)
        # # max_len = float('-inf')
        # # for i in range(n):
        # #     temp = s[0:i] + s[i+1:n]

        # #     if isPalindrome(temp):
        # #         max_len = max(max_len, n-len(temp))

        # # return n - max_len
        
        # max_len = float('-inf')

        # def hasPalin(s, mp, k):            
        #     n = len(s)

        #     if k >= n:
        #         return
            
        #     i = 0
        #     temp = []
        #     while i < n:
        #         if mp[i]:
        #             temp.append(s[i])
        #         i += 1
        #     temp = "".join(temp)
        #     if isPalindrome(temp):
        #         nonlocal max_len
        #         max_len = max(max_len, len(temp))
            
        #     mp[k] = True
        #     take = hasPalin(s, mp, k+1)
        #     mp[k] = False
        #     not_take = hasPalin(s, mp, k+1)
        #     mp[k] = True

        # n = len(s)
        # mp = [False]*n

        # hasPalin(s, mp, 0)
        # return n - max_len
    
s=Solution()
print(s.minDeletions("aebcbda"))
print(s.minDeletions("geeksforgeeks"))

