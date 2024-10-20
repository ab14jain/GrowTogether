class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:

        intervals.sort(key=lambda x: x[0])

        priority_queue = []
        greater = 0

        #timelimit exceeded

        for interval in intervals:
            if priority_queue and interval[0] > priority_queue[0]:
                priority_queue.pop(0)
            # else:
            #     greater += 1
            # priority_queue.append(interval[1])
            # priority_queue.sort()

            priority_queue.append(interval[1])
        

        return len(priority_queue)



# intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
intervals = [[1,3],[5,6],[8,10],[11,13]]
# intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
s = Solution()
print(s.minGroups(intervals))
