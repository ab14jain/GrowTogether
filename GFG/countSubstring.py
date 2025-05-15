from collections import defaultdict


class Solution:
	def countSubstring(self, s):
		# code here

            # h_map = defaultdict(list)
            # n = len(s)
            # count = 0
            # for i in range(n):
            #     ch = s[i]
            #     count += len(h_map[ch]) + 1
            #     h_map[ch].append(i)

            # return count
			
            freq = [0]*26
            n = len(s)
            for i in range(n):
                freq[ord(s[i]) - ord('a')] += 1

            count = 0
            for i in range(26):
                count += (freq[i]*(freq[i]+1))//2

            
            return count

s=Solution()
print((s.countSubstring('abcab')))
print((s.countSubstring('aba')))

                

