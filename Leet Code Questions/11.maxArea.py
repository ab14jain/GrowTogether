class Solution:
    def maxArea(self, height: list[int]) -> int:

        # Approach 1: Brute Force
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        # max_water = 0
        # n = len(height)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         max_water = max(max_water, min(height[i], height[j]) * (j-i))

        # return max_water

        # Approach 2: Two Pointer
        # Time complexity: O(n)
        # Space complexity: O(1)

        n = len(height)
        left = 0
        right = n-1

        max_water = 0
        while left < right:
            max_water = max(max_water, min(height[left], height[right]) * (right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water

s=Solution()
print(s.maxArea([1,8,6,2,5,4,9,3,7])) # 49