import math


class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        # max_quantity = max(quantities)

        # def canDistriibute(q, m, n):
        #     for i in q:
        #         n -= (i + m - 1) // m

        #         # print(m,n)

        #     return n >= 0

        # l = 1
        # r = max_quantity
        # m = (l+r)//2
        # ans = max_quantity
        # while l <= r:
        #     m = l + (r-l)//2

        #     if canDistriibute(quantities[:], m, n):
        #         ans = min(ans, m)
        #         r = m - 1
        #     else:
        #         l = m + 1

        # return ans

        def isPossible(arr, max_quantity, store_count):
            count = 0
            for i in range(len(arr)):
                count += math.ceil(arr[i]/max_quantity)

            if count <= store_count:
                return True
            
            return False
        
        low = 1
        high = max(quantities)
        ans = 0
        while low <= high:
            mid = low + (high - low)//2
            if isPossible(quantities[:], mid, n):  
                ans = mid
                high = mid - 1   
            else:                
                low = mid + 1
                
        return ans

    

s= Solution()
print(s.minimizedMaximum(6, [11,6])) # 3
print(s.minimizedMaximum(7, [15, 10, 10])) # 5
print(s.minimizedMaximum(4, [1,2,3,4])) # 4
print(s.minimizedMaximum(4, [1,2,3,4,5])) # 5
print(s.minimizedMaximum(4, [1,2,3,4,5,6])) # 6
print(s.minimizedMaximum(4, [1,2,3,4,5,6,7])) # 7