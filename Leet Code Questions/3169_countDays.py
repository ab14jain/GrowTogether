from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        # day_arr = [False]*(days+1)
        # for s,e in meetings:
        #     for i in range(s,e+1):
        #         day_arr[i] = True

        # count = 0
        # for i in range(1, len(day_arr)):
        #     if day_arr[i] == False:
        #         count += 1

        # return count
        
        meetings.sort()
        n = len(meetings)
        
        merged_meeting = []

        for i in range(n):
            start = meetings[i][0]
            end = meetings[i][1]

            if merged_meeting and merged_meeting[-1][1] >= end:
                continue

            for j in range(i + 1, n):
                if meetings[j][0] <= end:
                    end = max(end, meetings[j][1])
            merged_meeting.append([start, end])

        count = 0
        prev = 0
        for i in range(len(merged_meeting)):
            start = merged_meeting[i][0]
            end = merged_meeting[i][1]

            count += merged_meeting[i][0] - 1 - prev
            prev = end

        count += days - prev
        return count
    

s=Solution()
print(s.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]]))
print(s.countDays(days = 5, meetings = [[2,4],[1,3]]))
print(s.countDays(days = 6, meetings = [[1,6]]))