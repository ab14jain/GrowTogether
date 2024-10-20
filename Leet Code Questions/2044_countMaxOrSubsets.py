class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:

        maxXOR = 0

        for i in range(len(nums)):
            maxXOR |= nums[i]
        
        print(maxXOR)
        count = 0
        
        for i in range(1, 1 << len(nums)):
            temp = 0
            for j in range(len(nums)):
                if i & (1 << j):
                    temp |= nums[j]
            if temp == maxXOR:
                count += 1
        return count
    

s = Solution()
print(s.countMaxOrSubsets([3,1]))
print(s.countMaxOrSubsets([2,2,2]))
print(s.countMaxOrSubsets([3,2,1,5]))
print(s.countMaxOrSubsets([3,2,1,5,6]))
print(s.countMaxOrSubsets([3,2,1,5,6,7]))
        