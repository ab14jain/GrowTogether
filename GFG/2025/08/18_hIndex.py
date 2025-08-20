from typing import Counter


class Solution:
    def hIndex(self, citations):
        #code here
        # l = 0
        # h = max(citations)

        # ans = l

        # def get_count(num):
        #     count = 0

        #     for c in citations:
        #         if num <= c:
        #             count += 1
            
        #     return count

        # def bin_search(l, h):

        #     while l <= h:
        #         mid = l + (h-l)//2
        #         if get_count(mid) >= mid:
        #             nonlocal ans
        #             ans = max(ans, mid)
        #             l = mid + 1                    
        #         else:
        #             h = mid-1
                    
        #     return ans
        

        # return bin_search(l,h)

        n = len(citations)
        freq = [0]*(n+1)

        for citation in citations:
            if citation >= n:
                freq[n] += 1
            else:
                freq[citation] += 1
        
        s = freq[n]
        idx=n
        while s < idx:
            idx -= 1
            s += freq[idx]

        return idx          


    
s=Solution()
print(s.hIndex([8, 12, 10, 12, 9, 12]))
print(s.hIndex([3, 2, 2, 2, 1, 1, 2]))
print(s.hIndex([0,0]))
print(s.hIndex([0,0,1,1]))
print(s.hIndex([3,0,3,5,0]))