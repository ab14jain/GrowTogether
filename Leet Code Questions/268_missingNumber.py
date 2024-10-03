class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        single_num = 0
        for i in nums:
            single_num ^= i
        #     if max_nums < i:
        #         max_nums = i 
        
        # single_num = 0
        # for i in range(max_nums):
        #     single_num ^= i
            

        return single_num


s = Solution()
print(s.missingNumber([3,0,1]))  # 2
print(s.missingNumber([0,1]))  # 2
print(s.missingNumber([1]))  # [0] becoz 0 is missing and array should start from 0 only [0, 1] not [1,2]