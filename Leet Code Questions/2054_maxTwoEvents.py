class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        memo = [[-1]*3 for _ in range(100001)]

        def binary_search(events, target):
            n = len(events)
            low = 0
            high = n - 1
            result = n

            while low <= high:
                mid = low + (high - low) // 2                
                if events[mid][0] > target:
                    high = mid - 1
                    result = mid
                else:
                    low = mid + 1
                    

            return result
        
        def get_count(events, i, count):

            if count == 2 or i == len(events):
                return 0

            if memo[i][count] != -1:
                return memo[i][count]   
            
            next_event = binary_search(events, events[i][1])

            attended = events[i][2] + get_count(events, next_event, count+1)
            not_attended = get_count(events, i+1, count)

            memo[i][count] = max(attended, not_attended)
            return memo[i][count]


        events.sort(key = lambda x:x[0])        
        n = len(events)
        count = 0
        return get_count(events, 0, count)


s= Solution()
print(s.maxTwoEvents([[1,2,4],[3,4,3],[2,3,1]])) # 7
print(s.maxTwoEvents([[1,2,4],[3,4,3],[2,3,10]])) # 10
print(s.maxTwoEvents([[1,2,4],[3,4,3],[2,3,1],[4,5,1]])) # 8

        
        
        