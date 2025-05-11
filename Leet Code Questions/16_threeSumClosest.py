from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest_sum = float('inf')           
        for i in range(n):
            first = nums[i]
            left = i+1
            right = n-1
            while left < right:
                second = nums[left]
                third = nums[right]
                t_sum = first + second + third

                if abs(t_sum - target) < abs(closest_sum - target):
                    closest_sum = t_sum
                if t_sum == target:
                    return t_sum
                elif t_sum < target:
                    left += 1                        
                else:
                    right -= 1

        return closest_sum