class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        n = len(nums)        
        if n < 3:
            return []
        
        # res = set()
        # for i in range(n):
        #     target = -nums[i]
        #     seen = set()
        #     for j in range(i+1, n):            
        #         to_find = target - nums[j]    
        #         if to_find in seen:
        #             # triplet = {nums[i], nums[j], to_find}
        #             # triplet = sorted(triplet)
        #             # res.add(triplet)
        #             res.add(tuple(sorted([nums[i], nums[j], to_find])))

                
        #         seen.add(nums[j])
        

        res = []
        nums.sort()        
        i = 0      
        while i < n:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            first = nums[i]
            j = i + 1
            k = n - 1
            while j < k:                               
                second = nums[j]
                third = nums[k]
                total = first + second + third
                if total == 0:
                    res.append([first, second, third])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1                     
                elif total < 0:
                    j += 1
                else:
                    k -= 1

            i += 1


        return res
    
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
# print(s.threeSum([])) # []
# print(s.threeSum([0])) # []

                    