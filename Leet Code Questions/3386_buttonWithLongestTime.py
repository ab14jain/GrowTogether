class Solution:
    def buttonWithLongestTime(self, events: list[list[int]]) -> int:

        time_map = {}
        n = len(events)
        prev = 0
        idx = float('inf')
        max_time_taken = -float('inf')
        for i in range(n):

            event = events[i]
            time_taken = event[1] - prev
            prev = event[1]
            
            if max_time_taken <= time_taken:
                if idx > event[0]:
                    idx = event[0]
                max_time_taken = time_taken

            if event[0] in time_map:
                if time_taken > time_map[event[0]]:
                    time_map[event[0]] = time_taken
            else:
                time_map[event[0]] = time_taken
        
        return idx


s= Solution()
# print(s.buttonWithLongestTime([[1,2],[2,5],[3,9],[1,15]])) # 1
# print(s.buttonWithLongestTime([[1,2],[2,3],[3,4],[2,5]])) # 1
print(s.buttonWithLongestTime([[9,4],[19,5],[2,8],[3,11],[2,15]])) # 1