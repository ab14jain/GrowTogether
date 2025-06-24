class Solution:
    def maxSubseq(self, s, k):
        #code here

        # words = [""]
        # n = len(s)
        # def recur(s, idx, res, k):           

        #     if len(res) == k:
        #         nonlocal words
        #         words[0] = max(words[0], res)
        #         return

        #     if idx >= len(s):
        #         return
            
            
        #     recur(s,idx+1,res+s[idx],k)            
        #     recur(s,idx+1,res,k)

        # res = ""
        # recur(s, 0, res, n-k)
        
        # return words[0]

        n = len(s)
        res = ""
        # Keep a separate copy of k
        to_remove = k  

        # Build the result greedily
        for i in range(n):
            while res and to_remove > 0 and res[-1] < s[i]:
                res = res[:-1]
                to_remove -= 1
            res += s[i]
        
        # Result should be of length n - k
        return res[:n - k]

s=Solution()
print(s.maxSubseq("ritz", 2))
print(s.maxSubseq("zebra", 3))


        
