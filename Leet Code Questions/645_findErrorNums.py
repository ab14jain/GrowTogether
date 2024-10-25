class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        duplicate = -1
        missing = -1
        visited = [0]*n

        for i in range(n):            
            if visited[nums[i]-1]:
                duplicate = nums[i]
            else:
                visited[nums[i]-1] = 1
        
        for i in range(n):            
            if visited[i] == 0:
                missing = i + 1
        
        return [duplicate, missing]            
    
s = Solution()
print(s.findErrorNums([1,2,2,4]))
print(s.findErrorNums([1,1]))
print(s.findErrorNums([2,2]))
print(s.findErrorNums([3,2,3,4,6,5]))