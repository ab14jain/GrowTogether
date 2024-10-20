class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        n = len(times)
        target = times[targetFriend][0]
        chairs = [-1] * n
        times.sort()

        for i in range(n):
            
            arrival_time = times[i][0]
            departure_time = times[i][1]

            for j in range(n):
                if chairs[j] <= arrival_time:
                    chairs[j] = departure_time

                    if arrival_time == target:
                        return j
                    break

            
        
        return -1
    
s = Solution()
times = [[1,4],[2,3],[4,6]]
targetFriend = 1

print(s.smallestChair(times, targetFriend))
