from typing import List


class Solution:  
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        x_events = []
        y_events = []

        for cordinates in rectangles:
            x_events.append([cordinates[0],cordinates[2]])
            y_events.append([cordinates[1],cordinates[3]])


        def merge_events(axis):
            axis.sort()
            merged = []
            for i in range(len(axis)):
                start = axis[i][0]
                end = axis[i][1]

                if merged and merged[-1][1] >= end:
                    continue

                for j in range(i+1, len(axis)):
                    next_start = axis[j][0]
                    next_end = axis[j][1]
                    if next_start < end:
                        end = max(end, next_end) 
                
                merged.append([start, end])
            return merged
        
        x_events = merge_events(x_events)

        if len(x_events) >= 3:
            return True
        
        y_events = merge_events(y_events)

        return len(y_events) >= 3     
        
        

s=Solution()
print(s.checkValidCuts(n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))
print(s.checkValidCuts(n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]))