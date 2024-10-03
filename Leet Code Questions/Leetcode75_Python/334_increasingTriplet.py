import math
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        nums_len = len(nums)
        # i = 0

        # if (nums_len >= 3):
        #     while(i <= nums_len - 3):
        #         if (nums[i] < nums[i+1] and nums[i+1] < nums[i+2]):   
        #                 return True
        #         i += 1
        # return False

        first = math.inf
        second = math.inf

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:  # first < num <= second
                second = num
            else:
                print(f"first: {first}, second: {second}, num: {num}")
                return True  # first < second < num (third)

        return False
    
# Test
#nums = [4,8,6,5,2,2,7]
#nums = [20,100,10,12,5,13]
nums = [1,0,2,1,0,2]
solution = Solution()
print(solution.increasingTriplet(nums))