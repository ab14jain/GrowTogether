class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        
        n = len(nums)

        res_map = {}
        curr_sum = 0
        result = 0
        for i in range(n):
            curr_sum += nums[i]

            res = curr_sum % k

            if curr_sum % k == 0:
                result += 1
            
            if res in res_map:
                result += res_map[res]

            if res in res_map:
                res_map[res] += 1
            else:
                res_map[res] = 1
        
        return result



s=Solution()
print(s.subarraysDivByK([4,5,0,-2,-3,1], 5)) # 7
print(s.subarraysDivByK([5], 9)) # 0
print(s.subarraysDivByK([5,5], 9)) # 1