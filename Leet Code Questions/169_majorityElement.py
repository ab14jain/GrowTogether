class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        count_major = 0
        major_element = nums[0]

        for i in range(len(nums)):
            if count_major == 0:
                major_element = nums[i]
                count_major += 1
            elif major_element == nums[i]:
                count_major += 1
            else:
                count_major -= 1
        
        return major_element        
    

s = Solution()
print(s.majorityElement([1,1,2,2,3,3,3,3]))
# print(s.majorityElement([1]))
# print(s.majorityElement([1,2]))