class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        if len(nums) == 0:
            return 0       
        
        i = 0
        j = 1

        # need to replace in place using two pointers
        while  j < len(nums):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
            j += 1         
           
        
        return nums

s = Solution()
# print(s.removeDuplicates([1,1,2])) # 2
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5
# print(s.removeDuplicates([1,1,1,1,1,1,1,1])) # 1
# print(s.removeDuplicates([1])) # 1
# print(s.removeDuplicates([])) # 0
# print(s.removeDuplicates([1,2,3,4,5])) # 5
# print(s.removeDuplicates([1,1,1,2,2,3,3,4,4,5])) # 5
# print(s.removeDuplicates([1,1,1,1,1,2,2,2,2,2])) # 2
# print(s.removeDuplicates([1,1,1,1,1,1,1,1,1,1])) # 1
