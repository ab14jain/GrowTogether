class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:        
        n = len(nums)

        res = 0

        l = 0
        r = 0

        range_max = -float('inf')
        range_min = float('inf')
        while r < n:
            
            t_range_max = max(range_max, nums[r])
            t_range_min = min(range_min, nums[r])

            if abs(t_range_max - t_range_min) >= 0 and abs(t_range_max - t_range_min) <= 2:
                pass
            else:
                range_count = r - l
                res += range_count * (range_count + 1)//2
                l = r

                while l >= 0 and abs(nums[l] - nums[r]) <= 2:
                    t_range_max = max(range_max, nums[l])
                    t_range_min = min(range_min, nums[l])
                    l -= 1
                
                l += 1
                #count contribution before r index
                count = r - 1 - l + 1
                contri = count * (count + 1)//2
                res -= contri
        
            range_max = t_range_max
            range_min = t_range_min
            r += 1
        
        # for the last range
        range_count = r - l
        res += range_count * (range_count + 1)//2

        return res



        
    

s = Solution()
print(s.continuousSubarrays([1,2,3,4])) # 10
# print(s.continuousSubarrays([1,2,3,4,5])) # 15
# print(s.continuousSubarrays([1,2,3,4,5,6])) # 21