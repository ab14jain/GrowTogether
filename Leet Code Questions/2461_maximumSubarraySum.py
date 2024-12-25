class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)

        if n == 0:
            return 0
        
        nums_set = set()


        # i = 0
        # l = 0
        # max_unique_sum = 0
        # while i < n:
        #     if len(nums_set) == k:
        #         max_unique_sum = max(max_unique_sum, sum(nums_set))
            
        #     if nums[i] in nums_set:                
        #         while nums[l] != nums[i]:                    
        #             nums_set.remove(nums[l])                    
        #             l += 1
        #         nums_set.remove(nums[l])       
        #         l += 1        
            
        #     nums_set.add(nums[i])
        #     i += 1

        # return max_unique_sum

        i = 0
        j = 0
        max_unique_sum = 0        
        current_sum = 0 
        while j < n:            
            while nums[j] in nums_set:
                current_sum -= nums[i]
                nums_set.remove(nums[i])
                i += 1
            
            current_sum += nums[j]
            nums_set.add(nums[j])

            if (j-i+1) == k:
                max_unique_sum = max(max_unique_sum, current_sum)
                nums_set.remove(nums[i])
                current_sum -= nums[i]                
                i += 1            
            j += 1           
            
           
        return max_unique_sum
    
# Time complexity: O(n)
# Space complexity: O(k)

s=Solution()
print(s.maximumSubarraySum([1,2,1,2,3], 2)) # 5
# print(s.maximumSubarraySum([1,2,1,3,4], 3)) # 8
# print(s.maximumSubarraySum([1,2,1,3,4], 4)) # 10

        