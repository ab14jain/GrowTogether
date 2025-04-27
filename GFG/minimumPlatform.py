import heapq


class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here

        intervals = []

        for i in range(len(arr)):
            intervals.append([arr[i], dep[i]])

        intervals.sort()

        print(intervals)

        min_heap = []
        max_platforms = 1
        heapq.heappush(min_heap, intervals[0])
        i = 1
        while min_heap and i < len(arr):          

            while min_heap and min_heap[0][1] < intervals[i][0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, intervals[i])
            i += 1
            max_platforms = max(max_platforms, len(min_heap))

        return max_platforms
    

s=Solution()
print(s.minimumPlatform([1114, 825, 357, 1415, 54], [1740, 1110, 2238, 1535, 2323]))
# print(s.minimumPlatform([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]))