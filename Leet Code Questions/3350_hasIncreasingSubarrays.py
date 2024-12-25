class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        max_k = -float('Inf')
        k = n // 2
        while k > 0:            
            i = k - 1            
            while i < n - k:
                l = i - 1
                r = i + 1
                curr = nums[i]
                left_count = 0
                left_array = [curr]
                right_array = [nums[r]]
                while (l >= 0 and nums[l] < curr and left_count < (k - 1)):
                    left_array.append(nums[l])
                    curr = nums[l]
                    l -= 1        
                    left_count += 1
                
                curr = nums[r]            
                right_count = 0
                while (r < n - 1 and nums[r + 1] > curr and right_count < (k - 1)):
                    r += 1
                    right_array.append(nums[r])
                    curr = nums[r]
                    right_count += 1            
                
                if len(left_array) == k and len(right_array) == k:
                    max_k = max(max_k, k) 
                i += 1
            
            k -= 1
        
        return max_k
    

s= Solution()
print(s.maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1])) # 3
print(s.maxIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7])) # 2