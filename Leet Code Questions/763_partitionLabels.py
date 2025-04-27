from collections import defaultdict
from typing import Counter, List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last_idx_map = defaultdict(int)
        n = len(s)
        for i in range(n):
            last_idx_map[ord(s[i])-97] = i            

        i = 0
        start = 0
        end = last_idx_map[ord(s[0])-97]        
        ans = []
        while i < n:
            end = max(end, last_idx_map[ord(s[i])-97])

            if i == end:
                ans.append(end-start+1)
                start = end+1
            i += 1
        return ans
    
    
        # while end < n:
        #     while j < end:                
        #         end = max(end, last_idx_map[ord(s[j])-97])                
        #         j += 1
            
        #     ans.append(j-i+1)
        #     i = j+1
        #     j = j+1

        #     if i >= n or j >= n:
        #         break
        #     end = max(end, last_idx_map[ord(s[i])-97])
        
        # return ans
        
        # ans = []
        # l = 0
        # r = last_i
        # while r < n:

        #     is_True = True
        #     for j in range(l+1, last_i):
        #         if last_idx[ord(s[j])-97] > last_i:    
        #             is_True = False 
        #             last_i = last_idx[ord(s[j])-97]               
        #             break
            
        #     if is_True:
        #         next_idx = last_i+1-l
        #         ans.append(next_idx)

        #         l = first_idx[ord(s[next_idx])-97]
        #         r = last_idx[ord(s[next_idx])-97]
        #         last_i = r
           
            


        
        

s=Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))
print(s.partitionLabels("eccbbbbdec"))