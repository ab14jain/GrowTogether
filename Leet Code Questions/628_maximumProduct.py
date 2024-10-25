
# Intuition
#<!-- Describe your first thoughts on how to solve this problem. -->



# Approach

# 1. Sort the input array.
# 2. Return the maximum of the product of the last three elements and the product of the first two elements and the last element.
# 3. The maximum product of three numbers is the product of the last three elements of the sorted array.

# Complexity
#- Time complexity:
# O(nlogn) - Sorting the input array.

#- Space complexity:
# O(1)

#Easiest ocde solved in nlogn time complexity

#Approach 2
# 1. Find the three maximum elements and two minimum elements in the input array.
# 2. Return the maximum of the product of the three maximum elements and the product of the two minimum elements and the maximum element.


class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        
        #nums.sort()
        print(nums)
        # return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        
        for num in nums:

            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            if min1 > num:
                min2 = min1
                min1 = num
            elif min2 > num:
                min2 = num

        print(max1, max2, max3, min1, min2)
        return max(max1 * max2 * max3, min1 * min2 * max1)
          

s = Solution()

print(s.maximumProduct([0,1,2,0,0,-3,-4,-2,-1])) # 20
# print(s.maximumProduct([0,1,2,3,4,-3,-4,-2,-1])) # 48
# print(s.maximumProduct([0,1,2,0,0,-3,-4,-2,-1])) # 24
# print(s.maximumProduct([-1,-2,-3])) # -6
# print(s.maximumProduct([-1,-2,-3,0])) # 0
# print(s.maximumProduct([-1,-2,-3,0,1])) # 6