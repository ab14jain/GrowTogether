# Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->
#   - We can solve this problem by calculating the water trapped at each index.
#   - We can calculate the water trapped at each index by taking the minimum of the maximum height of the left and right side of the index.
#   - The trapped water at each index will be the minimum of the maximum height of the left and right side of the index minus the height of the index.
#   - We can calculate the maximum height of the left and right side of the index by iterating through the array and storing the maximum height of the left and right side of the index.
#   - Finally, we can sum up the trapped water at each index to get the total trapped water.

# Approach
# <!-- Describe your approach to solving the problem. -->
#   - We can implement the above approach using dynamic programming.
#   - We can create two arrays left_max and right_max to store the maximum height of the left and right side of the index.
#   - We can iterate through the array and calculate the maximum height of the left and right side of the index and store it in the left_max and right_max arrays.
#   - We can iterate through the array and calculate the trapped water at each index and sum it up to get the total trapped water.
#   - Finally, we can return the total trapped water.

# Complexity
#- Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
# The time complexity of this approach is O(n)


#- Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
# The time complexity of this approach is O(n)

class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        left_max = [0]*n
        right_max = [0]*n
        left_max[0] = height[0]
        right_max[n-1] = height[n-1]

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
            right_max[n - i - 1] = max(right_max[n - i], height[n - i - 1])
        
        result_sum = 0
        for i in range(n):
            temp_sum = min(left_max[i], right_max[i]) - height[i]

            if(temp_sum):
                result_sum += temp_sum
        
        return result_sum

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(s.trap([4,2,0,3,2,5])) # 9
