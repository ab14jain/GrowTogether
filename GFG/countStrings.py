# https://www.geeksforgeeks.org/problems/exactly-one-swap--170637/1

from typing import Counter


class Solution:
    def countStrings(self, s): 
        #code here

        # counter = Counter(s)
        # strings = set()
        # n = len(s)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         ts = list(s)
        #         ts[i],ts[j] = ts[j],ts[i]
        #         strings.add("".join(ts))

        # return len(strings)
        
        freq = [0]*26


        n = len(s)
        count = 0
        for i in range(n):
            count += (i - freq[ord(s[i]) - ord('a')])
            freq[ord(s[i]) - ord('a')] += 1

        for i in range(26):
            if freq[i] > 1:
                count += 1
                break

        return count


s=Solution()
print(s.countStrings("geek"))
print(s.countStrings("aaaa"))