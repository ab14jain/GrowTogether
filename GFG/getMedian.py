#https://www.geeksforgeeks.org/problems/find-median-in-a-stream-1587115620/1

import heapq


class Solution:
    def getMedian(self, arr):

        h1 = [] #max_heap
        h2 = [] #min_heap


        def get_median(num):

            if len(h1) == 0 or num <= -h1[0]:
                heapq.heappush(h1, -num)
            else:
                heapq.heappush(h2, num)

            if len(h2) > len(h1):
                temp = heapq.heappop(h2)
                heapq.heappush(h1, -temp)

            if len(h1) - len(h2) == 2:
                temp = heapq.heappop(h1)
                heapq.heappush(h2, -temp)

            if len(h1) > len(h2):
                return -h1[0]
            else:
                return (-h1[0] + h2[0])/2
            
        ans = []
        for num in arr:
            ans.append(get_median(num))

        return ans


s=Solution()
print(s.getMedian([5,15,1,3,2,8]))
