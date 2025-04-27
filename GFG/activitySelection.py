#https://www.geeksforgeeks.org/problems/activity-selection-1587115620/1

import heapq


class Solution:
    def activitySelection(self, start, finish):
        #code here
        # task = []

        # for i in range(len(start)):
        #     task.append([start[i], finish[i]])

        # task.sort()

        # print(task)

        ans = 0        
        p = []
        for i in range(len(start)):
            heapq.heappush(p, (finish[i], start[i]))        
        finishtime = -1
        while p:
            task = heapq.heappop(p)
            if task[1] > finishtime:
                finishtime = task[0]
                ans += 1

        return ans

s=Solution()
print(s.activitySelection([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))