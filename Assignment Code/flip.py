class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        # solution 1: Kadane's algorithm
        # Intution
        # 1. Iterate through the string and check for 0s and 1s
        # 2. If 0 is found, increment the count
        # 3. If 1 is found, decrement the count
        # 4. If the count is greater than the max_diff, update the max_diff
        # 5. Update the left and right indices
        # 6. Return the left and right indices
        # Time complexity: O(n)
        # Space complexity: O(n)

        n = len(A)
        
        l = 0
        r = 0
        current_sum = 0
        max_sum = 0
        ans = [0,0]
        res = [0] * n
        is_all_ones = True
        for i in range(n):
            if A[i] == '0':
                res[i] = 1
                is_all_ones = False       
            else:
                res[i] = -1

        if is_all_ones:
            return []

        for i in range(n):
            current_sum += res[i]
            if current_sum < 0:
                current_sum = 0
                l = i + 1
            if current_sum > max_sum:
                max_sum = current_sum
                ans[0] = l + 1
                ans[1] = i + 1
        
        return ans
               

       
#generate binary for 100000 length
import random
def randomString():
    return ''.join(random.choice('01') for _ in range(100000))

s = Solution()
# print(s.flip("010")) # [1, 1]

binary_string = randomString()
print(binary_string)
print(s.flip(binary_string)) # [1, 1]
print(s.flip('111010100011011001111011111000011111001101010100011011000001110101000001100101110010010001101110011100000101011000011011111001110111011101011101011001010000001111100110100011010111010111001110110101011110011111110')) # [1, 1]


