class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = -1
       
        min_index = -1
        for i in range(n-1, -1, -1):
            if nums[i] > nums[i-1]:
                index = i                
                break
        
        if index > 0:
            temp_index = index
            swap_number = nums[index-1]
            just_greater_than_swap = float('Inf')
            while temp_index < n:
                if nums[temp_index] > swap_number:
                    just_greater_than_swap = min(just_greater_than_swap, nums[temp_index])
                    min_index = temp_index
                temp_index += 1
            
            if min_index != -1:
                nums[i-1], nums[min_index] = nums[min_index], nums[i-1]
            else:
                nums[i-1], nums[i] = nums[i], nums[i-1]
        

        i = n-1
        j = index
        while i > j:
            nums[i], nums[j] = nums[j], nums[i]
            i -= 1
            j += 1

        print(nums)

# Driver code
s = Solution()
# nums = [3,1,6,4,2,0]
# s.nextPermutation(nums) # 2 2
# nums = [3, 2, 1]
s.nextPermutation([3, 2, 1]) # -1 3
#s.nextPermutation([3,1,6,1,4,7,6,5,4])
# s.nextPermutation([2,3,1])
# s.nextPermutation([3,1,6,2,4,0])
