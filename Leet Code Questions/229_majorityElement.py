class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)      
             
        first_count = 0
        second_count = 0
        i = 0
        first_majority = nums[i]
        second_majority = -1
        while i < n:
            if first_majority == nums[i]:
                first_count += 1
            elif second_majority == nums[i]:
                second_count += 1
            elif first_count == 0:
                first_majority = nums[i]
                first_count = 1
            elif second_count == 0:
                second_majority = nums[i]
                second_count = 1
            else:
                first_count -= 1
                second_count -= 1 
            
            i += 1           


        freq_first = 0
        freq_second = 0
        for i in range(n):
            if nums[i] == first_majority:
                freq_first += 1
            elif nums[i] == second_majority:
                freq_second += 1
        res = []
        if freq_first > n//3:
            res.append(first_majority)
        
        if freq_second > n//3:
             res.append(second_majority)
            
        
        return res
    

s = Solution()
# print(s.majorityElement([3,2,3]))
# print(s.majorityElement([1]))
print(s.majorityElement([1,2]))
# print(s.majorityElement([1,2,3]))