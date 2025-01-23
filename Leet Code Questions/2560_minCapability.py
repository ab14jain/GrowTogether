class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        
        # Approach 1: Brute Force
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        # n = len(nums)
        # min_capability = float('inf')
        # for i in range(n):
        #     for j in range(i+1, n+1):
        #         if j-i >= k:
        #             min_capability = min(min_capability, max(nums[i:j]))
        # 
        # return min_capability

        # Approach 2: Binary search
        # Time complexity: O(n)
        # Space complexity: O(1)

        def check_capability(capability: int) -> bool:
            n = len(nums)
            cnt = 0
            for i in range(n):
                if nums[i] <= capability:
                    cnt += 1
                else:
                    cnt = 0
                if cnt == k:
                    return True
            return False

        left = 1
        right = max(nums)
        while left < right:
            mid = left + (right-left)//2
            if check_capability(mid):
                right = mid
            else:
                left = mid+1
        
        return left
        
    
s=Solution()
print(s.minCapability([1,2,3,4,5], 2)) # 2
print(s.minCapability([3,2,1,5,4], 2)) # 3