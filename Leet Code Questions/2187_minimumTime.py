class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        
        def isPossible(t, tripcount):
            count = 0
            n = len(t)
            for i in range(n):
                count += ((1*tripcount)//t[i])
            
            if count >= totalTrips:
                return True
            return False
        
        low = 1
        high = max(totalTrips, max(time))
        ans = 0
        while low <= high:
            mid = low + (high-low)//2

            if isPossible(time, mid):
                ans = mid
                high = mid - 1                
            else:
                low = mid + 1

        return ans
    
s=Solution()
print(s.minimumTime([5,10,10], 9)) # 3
print(s.minimumTime([3,3,3], 2)) # 3
# print(s.minimumTime([1,2,3], 5)) # 3
# print(s.minimumTime([1,2,3], 6)) # 3
# print(s.minimumTime([1,2,3], 7)) # 3
# print(s.minimumTime([1,2,3], 8)) # 3
# print(s.minimumTime([1,2,3], 9)) # 3
# print(s.minimumTime([999,999,999], 4)) # 3