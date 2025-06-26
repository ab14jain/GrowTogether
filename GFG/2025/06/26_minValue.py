import heapq
from typing import Counter


class Solution:
    def minValue(self, s, k):
        # code here
        counter = Counter(s)
        max_freq = []
        sq_sum = 0

        for c in counter:
            heapq.heappush(max_freq, -counter[c])

        while k and max_freq:
            curr = heapq.heappop(max_freq)     

            curr = (-curr) - 1       
            heapq.heappush(max_freq, -curr)

            k -= 1
            # if -curr <= k:
            #     k = k - (-curr)
            # else:
            #     rem = (-curr) - k
            #     k = 0
            #     heapq.heappush(max_freq, -rem)

        for num in max_freq:
            sq_sum += num*num

        return sq_sum

        # freq = [0] * 26

        # # Count frequency of each character
        # for c in s:
        #     freq[ord(c) - ord('a')] += 1

        # # Reduce the highest frequency character k times
        # while k > 0:
            
        #     # Sort so the max frequency is at the end
        #     freq.sort() 
            
        #     # No characters left to reduce
        #     if freq[25] == 0:
        #         break  
            
        #     # Reduce the max frequency
        #     freq[25] -= 1  
        #     k -= 1

        # # Calculate sum of squares of frequencies
        # result = sum(f * f for f in freq)
        # return result

s=Solution()
# print(s.minValue("abbccc", 2))
# print(s.minValue("aaab", 2))
print(s.minValue("aaabbbbbcccccccrrrrrrrsdfsdfsadfsdfsdfsdfasd", 25))
                

