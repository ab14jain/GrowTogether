class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:       

        # using set to remove duplicates - added sapce complexity to store the set
        # new_set = set(nums)

        # if len(new_set) == len(nums):
        #     return False
        # else:
        #     return True

        # using dictionary to store the count of each element
        new_dict = {}
        for i in nums:
            if i in new_dict:
                return False
            else:
                new_dict[i] = 1
        return True
    
s = Solution()
print(s.containsDuplicate([1,1,2,3,4,5,6,7,8,9,10,10]))  # False
            