class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        new_dict = {}
        for i in range(len(nums)):
            if nums[i] in new_dict:
                if abs(new_dict[nums[i]] - i) <= k:
                    return True
            new_dict[nums[i]] = i
           
        return False

        # hashMap = {}
        # for i in range(len(nums)):
        #     if nums[i] in hashMap:
        #         if abs(i - hashMap[nums[i]]) <= k:
        #             return True
        #     hashMap[nums[i]] = i
        # return False

s = Solution()
print(s.containsNearbyDuplicate([1,0,1,1], 1))  # False