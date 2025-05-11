#Intution
# 1. Create a dictionary to store the index of the numbers
# 2. Loop through the list of numbers
# 3. Find the difference between the target and the number

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        counter_nums = {}
        for i in range(len(nums)):
            if nums[i] in counter_nums:
                counter_nums[nums[i]].append(i)
            else:
                counter_nums[nums[i]] = [i]

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff == nums[i]:
                if len(counter_nums[diff]) > 1:
                    return [counter_nums[diff][0],counter_nums[diff][1]]
            else:
                if diff in counter_nums:
                    return [i, counter_nums[diff][0]]

        #return counter_nums
        

test = Solution()
print(test.twoSum([2,7,11,15], 26)) # [0, 1]
print(test.twoSum([3,3], 6)) # [0, 1]
print(test.twoSum([3, 2, 4], 6)) # [1, 2]


        