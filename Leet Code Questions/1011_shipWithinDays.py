class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        
        def isPossible(arr, days, load):
            count = 1
            capacity = 0            
            n = len(arr)

            for i in range(n):
                capacity += arr[i]

                if capacity > load:
                    capacity = arr[i]
                    count += 1
                
            
            if count <= days:
                return True

            return False

        
        low = max(weights)
        high = sum(weights)
        ans = 0

        while low <= high:

            mid = low + (high - low)//2

            if isPossible(weights, days, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        
        return ans           

s=Solution()
print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)) # 15
print(s.shipWithinDays([3,2,2,4,1,4], 3)) # 6