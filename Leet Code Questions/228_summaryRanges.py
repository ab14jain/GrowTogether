class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res = []
        i = 0
        j = 1
        n = len(nums)        
             
        while j < n: 
            if  nums[j] - nums[j-1] == 1:
                if j == n - 1:
                    ranges = str(nums[i]) + "->" + str(nums[j])
                    res.append(ranges)
                    break
                else:
                    j += 1
                continue
            else:
                if i == j - 1:
                    res.append(str(nums[i]))
                    i = j
                else:
                    ranges = str(nums[i]) + "->" + str(nums[j-1])
                    res.append(ranges)
                    i = j

            if i == n - 1:
                res.append(str(nums[i]))
                break
            j = j + 1
        
        
        return res


s = Solution()

# print(s.summaryRanges([0,1,2,4,5,7]))
# print(s.summaryRanges([0,2,3,4,6,8,9]))
# print(s.summaryRanges([0,2,3,5,7,9]))
# print(s.summaryRanges([0,2,3,5,7,9,11]))
print(s.summaryRanges([0,2,3,4,6,8,9]))