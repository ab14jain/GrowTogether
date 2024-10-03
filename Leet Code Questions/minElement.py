class Solution:
    def minElement(self, nums: list[int]) -> int:

        min_num = 100000
        for i in nums:
            digit_sum = 0
            while(i != 0):
                digit_sum += int(i%10)
                i = int(i/10)
            
            if digit_sum < min_num:
                min_num = digit_sum
        
        return min_num

s = Solution()
print(s.minElement([10,12,13,14]))  # 1