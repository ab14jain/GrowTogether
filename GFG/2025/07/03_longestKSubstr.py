class Solution:
    def longestKSubstr(self, s, k):
        # code here
        
        mp = {}
        i = 0
        j = 0
        n = len(s)
        ans = 0
        runn_ans = 0

        while i < n:
            if s[i] in mp:
                mp[s[i]] += 1
            else:
                mp[s[i]] = 1
          
            runn_ans += 1

            if len(mp) == k:    
                ans = max(ans, runn_ans)

            while len(mp) > k and j < i:
                mp[s[j]] -= 1
                if mp[s[j]] == 0:
                    del mp[s[j]]
                     
                j += 1
                runn_ans -= 1

            i += 1

        if ans == 0:
            return -1
        return ans

s=Solution()
print(s.longestKSubstr("mlg", 1))
print(s.longestKSubstr("mlg", 3))
print(s.longestKSubstr("aabacbebebe", 3))
print(s.longestKSubstr("aaaa", 2))
print(s.longestKSubstr("aabaaab", 2))

        
        