from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
                
        n = len(nums)
        mp = {}
        count = 0
        hasDuplicate = False

        for i in range(n):
            if nums[i] in mp:
                mp[nums[i]] += 1
                hasDuplicate = True
            else:
                mp[nums[i]] = 1

        x = 0
        while hasDuplicate:

            if n-x == 0:
                return count
            if n - x <= 2:
                hasDuplicate = False
                count += 1
                break

            for i in range(x, x+3):
                mp[nums[i]] -= 1
            
            
            x += 3
            for i in range(x, n):
                if mp[nums[i]] > 1:
                   hasDuplicate = True
                   break 
                else:
                    hasDuplicate = False
            
            count += 1
        return count

        # n = len(nums)
        # mp = {}
        # count = 0
        # hasDuplicate = False

        # for i in range(n):
        #     if nums[i] in mp:
        #         mp[nums[i]] += 1
        #         hasDuplicate = True
        #     else:
        #         mp[nums[i]] = 1

        # x = 0
        # while hasDuplicate:

        #     for i in range(x, min(x+3, n)):
        #         mp[nums[i]] -= 1
            
        #     if n-x-3 == 2:
        #         hasDuplicate = False
        #     x += 3

        #     for i in range(x, n):
        #         if mp[nums[i]] > 1:
        #            hasDuplicate = True
        #            break 
        #         else:
        #             hasDuplicate = False
            
        #     count += 1
        # return count
        # # hasDuplicate = False
        # # for i in range(n):
        # #     if nums[i] in mp:
        # #         mp[nums[i]] += 1
        # #         hasDuplicate = True
        # #     else:
        # #         mp[nums[i]] = 1

        # # count = 0
        # # while hasDuplicate:

        # #     for i in range(3):
        # #         mp[nums[i]] -= 1
                
            
        # #     for i in range(3, n):
        # #         if mp[nums[i]] > 1:
        # #            hasDuplicate = True
        # #            break 
        # #         else:
        # #             hasDuplicate = False
            
        # #     count += 1
            

        # # return count


s=Solution()
# print(s.minimumOperations([1,2,3,4,2,3,3,5,7]))
print(s.minimumOperations([2,2,13]))
# print(s.minimumOperations([4,5,6,4,4]))




            

