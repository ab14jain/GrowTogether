#https://www.geeksforgeeks.org/problems/non-overlapping-intervals/1

class Solution:
    def minRemoval(self, intervals):
        # Code here
        intervals.sort(key=lambda x: x[1])
        ans = 0
        overlapping = []        
        non_overlapping = []
        
        last = intervals[0][1]       
        
        i = 1
        n = len(intervals)
        while i < n:
            if intervals[i][0] < last:
                overlapping.append(intervals[i])                
            else:
                last = intervals[i][1]
                non_overlapping.append(intervals[i])

            i += 1
                
        ans = len(overlapping)
        return ans 

        # cnt = 0

        # # Sort by minimum ending point
        # intervals.sort(key=lambda x: x[1])
        # non_overlappingN = []
        # overlappingN = []
        # end = intervals[0][1]

        # for i in range(1, len(intervals)):

        #     # if there is an overlap increase the count
        #     if intervals[i][0] < end:
        #         overlappingN.append(intervals[i])  
        #         cnt += 1

        #     # else increment the ending point
        #     else:
        #         end = intervals[i][1]
        #         non_overlappingN.append(intervals[i])  

        # # return the count
        # return cnt

s=Solution()
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(s.minRemoval(intervals)) #1
intervals = [[1, 2], [1, 2], [1, 2]]
print(s.minRemoval(intervals)) #2
intervals = [[1, 2],[5, 10],[18, 35],[6, 45],[42, 50]]
print(s.minRemoval(intervals)) #1
intervals = [[1, 2], [2, 3], [3, 5], [1, 4]]
print(s.minRemoval(intervals)) #1
intervals = [[29, 39],[68, 89],[62, 127],[1 ,62],[31, 114],[20, 85],[43, 63],[48, 85],[92, 149],[76, 163],[28, 120],
]
print(s.minRemoval(intervals)) #1