class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        i = k - 1

        while i < n - k:
            l = i - 1
            r = i + 1
            curr = nums[i]
            left_count = 0
            left_array = [curr]
            right_array = [nums[r]]
            while l >= 0 and nums[l] < curr and left_count < k - 1:
                left_array.append(nums[l])
                curr = nums[l]
                l -= 1        
                left_count += 1
            
            curr = nums[r]            
            right_count = 0
            while r < n - 1 and nums[r + 1] > curr and right_count < k - 1:
                r += 1
                right_array.append(nums[r])
                curr = nums[r]
                right_count += 1
            
            print(i, left_array, right_array)
            if len(left_array) == k and len(right_array) == k:
                return True
            i += 1
        
        return False
    
s= Solution()   
print(s.hasIncreasingSubarrays([1,1], 1)) # False
# print(s.hasIncreasingSubarrays([1,2,3,4,8,9], 3)) # True
# print(s.hasIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7], 5)) # False
# print(s.hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1], 3)) # True