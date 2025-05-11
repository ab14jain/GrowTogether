from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        

        # l = 0
        # r = 0
        # n = len(nums)

        # curr_sum = 0
        # xor_sum = 0
        # max_len = 0

        # while r < n:    
        #     curr_sum += nums[r]
        #     xor_sum ^= nums[r]                
        #     while curr_sum != xor_sum:                
        #         curr_sum -= nums[l]
        #         xor_sum ^= nums[l]  # For array [8,5,2,6] -> removing first element 8^(8^5^2)
        #         l += 1

        #     max_len = max(max_len, r-l+1)
        #     r += 1

        # return max_len

        def isNice(arr):
            n = len(arr)
            for i in range(n):
                for j in range(i+1, n):
                    if arr[i] & arr[j] != 0:
                        return False
            return True

        n = len(nums)
        max_len = 1
        for i in range(n):
            for j in range(i, n):
                # print(nums[i:j+1])
                if(isNice(nums[i:j+1])):
                    max_len = max(max_len, j-i+1)
                else:
                    break
        
        return max_len

s=Solution()
print(s.longestNiceSubarray([744437702,379056602,145555074,392756761,560864007,934981918,113312475,1090,16384,33,217313281,117883195,978927664]))
print(s.longestNiceSubarray([1,3,8,48,10]))
