import heapq
from typing import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        
        count = Counter(s)
        max_heap = [[-ord(c), count] for c, count in count.items()]
        res = []
        heapq.heapify(max_heap)
        while max_heap:
            c, count = heapq.heappop(max_heap)
            occurence = min(count, repeatLimit)
            res.append(chr(-c)*(occurence))            

            if count - repeatLimit > 0 and max_heap:
                c2, count2 = heapq.heappop(max_heap)
                occurence = min(count2, repeatLimit)
                res.append(chr(-c2))
                
                heapq.heappush(max_heap, [c, count - repeatLimit])
                if count2 > 1:
                    heapq.heappush(max_heap, [c2, count2 - 1])


            
        return "".join(res)
            



s= Solution()
print(s.repeatLimitedString("cczazcc", 3)) # "abc"
print(s.repeatLimitedString("aababab", 3)) # "abac"
print(s.repeatLimitedString("aaaaaaa", 2)) # "ab"