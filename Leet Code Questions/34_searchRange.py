class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        def lower_bound(num):
            low = 0
            high = n - 1
            while low <= high:
                mid = low + (high -low)//2
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return low

        def upper_bound(num):
            low = 0
            high = n - 1
            while low <= high:
                mid = low + (high -low)//2
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

            return high

        if lower_bound(target) > upper_bound(target):
            return [-1,-1]  

        return [lower_bound(target),upper_bound(target)]


s=Solution()
print(s.searchRange([5,7,7,8,8,10], 8)) # [3,4]
print(s.searchRange([5,7,7,8,8,10], 6)) # [-1,-1]


