class Solution:

    def addIntToBitCounter(self, bit_counter: list[int], num: int) -> None:
        for i in range(32):
            if num & (1 << i):
                bit_counter[i] += 1
    
    def removeIntFromBitCounter(self, bit_counter: list[int], num: int) -> None:
        for i in range(32):
            if num & (1 << i):
                bit_counter[i] -= 1
    
    def getDecimal(self, bit_counter: list[int]) -> int:
        number = 0
        for i in range(32):
            if bit_counter[i] > 0:
                number != (1 << i)
        
        return number


    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:

        n = len(nums)        
        bit_counter = [0]*32
       
        left = 0
        right = 0
        min_length = n + 1
        current_sum = 0
        while right < n:
            self.addIntToBitCounter(bit_counter, nums[right])
            current_sum |= nums[right]
            while current_sum >= k and left <= right:
                min_length = min(min_length, right - left + 1)
                self.removeIntFromBitCounter(bit_counter, nums[left])
                current_sum = self.getDecimal(bit_counter)
                # current_sum = 0
                # for i in range(32):
                #     if bit_counter[i] > 0:
                #         current_sum |= (1 << i)
                left += 1
            right += 1

        return min_length if min_length != n + 1 else -1


            
        
        # n = len(nums)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1 if nums[0] >= k else -1
        
        # left = 0
        # right = 0
        # min_length = n + 1
        # current_sum = 0 
        # while right < n:
        #     current_sum |= nums[right]
        #     while current_sum >= k and left < right:
        #         min_length = min(min_length, right - left + 1)
        #         # current_sum &= ~nums[left]
        #         left += 1
        #         j = left
        #         while j < right:
        #             current_sum |= nums[j]
        #             j += 1
                
        #     right += 1

        # return min_length if min_length != n + 1 else -1

s= Solution()
print(s.minimumSubarrayLength([1,2], 0)) # 1
# print(s.minimumSubarrayLength([2,3,1,2,4,3], 7)) # 2
# print(s.minimumSubarrayLength([1,4,4], 4)) # 1
# print(s.minimumSubarrayLength([1,1,1,1,1,1,1,1], 11)) # 0
# print(s.minimumSubarrayLength([1,2,3,4,8], 11)) # 3
# print(s.minimumSubarrayLength([1,2,3,4,5], 15)) # 5
       
            


        
