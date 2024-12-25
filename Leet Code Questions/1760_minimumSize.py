import math


class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:

        n = len(nums)
        ans = float('inf')

        low = 1
        high = max(nums)

        mid = low + (high - low) // 2

        while low <= high:
            nops = 0

            for i in range(n):
                nops += math.ceil((nums[i] - mid)/mid)
                if nops > maxOperations:
                    break
            
            if nops <= maxOperations:
                high = mid - 1
                ans = min(ans, mid)
            else:
                low = mid + 1


            mid = low + (high - low) // 2

        
        return ans
    

s= Solution()
# print(s.minimumSize([9], 2)) # 3
# print(s.minimumSize([2,4,8,2], 4)) # 2
# print(s.minimumSize([7,17], 2)) # 7
print(s.minimumSize([1,2,3,4,5], 2)) # 3