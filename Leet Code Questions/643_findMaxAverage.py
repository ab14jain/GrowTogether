class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        n = len(nums)
        if n == 0:
            return 0         

        x = 0
        window_sum = 0
        avg = 0
        while x < k:
            window_sum += nums[x]
            x += 1
        avg = window_sum/k

        i = k
        while i < n:            
            window_sum += nums[i] - nums[i-k]
            avg = max(avg, window_sum/k)
            i += 1  
        return max(avg)