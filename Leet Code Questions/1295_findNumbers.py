class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        #   Method - 1 Score = 6.83%
        # even_digit_count = 0
        # for i in range(len(nums)):

        #     count = 0
        #     d = nums[i]
        #     while d:
        #         count += 1
        #         d = d//10

        #     if count % 2 == 0:
        #         even_digit_count += 1
        
        # return even_digit_count

        # Method - 2 Score 40.60%
        # even_digit_count = 0
        # for i in range(len(nums)):
        #     if len(str(nums[i]))%2 == 0:
        #         even_digit_count += 1
        
        # return even_digit_count

        # Method - 3 Score 100%
        # even_digit_count = 0
        # for i in range(len(nums)):
        #     if (floor(log10(nums[i]))+1)%2 == 0:
        #         even_digit_count += 1
        
        # return even_digit_count

        # Method - 4 Score 100%
        # even_digit_count = 0
        # for i in range(len(nums)):
        #     if (ceil(log10(nums[i]+1)))%2 == 0:
        #         even_digit_count += 1
        
        # return even_digit_count

        # Method - 5 Score 100%
        even_digit_count = 0
        for i in range(len(nums)):
            if (10 <= nums[i] <= 99) or (1000 <= nums[i] <= 9999) or nums[i] == 100000:
                even_digit_count += 1
        
        return even_digit_count

