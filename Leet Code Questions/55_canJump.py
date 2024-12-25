class Solution:
    def canJump(self, nums: list[int]) -> bool:

        target = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= target:
                target = i
            
        if target == 0:
            return True
        return False

s= Solution()
print(s.canJump([2,3,1,1,4])) # True
print(s.canJump([3,2,1,0,4])) # False
print(s.canJump([0])) # True
print(s.canJump([1])) # True
print(s.canJump([0, 1])) # False
        