class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        
        # Approach 1: 91/101 test cases passed
        # n = len(nums)
        # prefix_sum = {}
        # curr_sum = 0
        # result = False
        # for i in range(n):            
        #     nums[i] %= k
        
        # for i in range(n):
            
        #     curr_sum += nums[i]

        #     if curr_sum % k == 0 and i > 0:
        #         result = True
        #         break
            
        #     if (curr_sum - k) in prefix_sum:
        #         result = True
        #         break
            
            
        #     prefix_sum[curr_sum] = 1
            

        # return result

        n = len(nums)
        prefix_sum = {0:-1}
        curr_sum = 0
        result = False

        for i in range(n):

            curr_sum += nums[i]

            res = curr_sum % k
            if res in prefix_sum:
                if i - prefix_sum[res] > 1:
                    return True
            else:
                prefix_sum[res] = i

        return result



s=Solution()
print(s.checkSubarraySum([23,23,8,7,7], 6)) # True
print(s.checkSubarraySum([23,2,4,6,7], 6)) # True
print(s.checkSubarraySum([23,2,4,6,8], 6)) # True
print(s.checkSubarraySum([23,2,6,4,7], 13)) # False