class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = []       
        n = len(nums)
        result = [-1]*n

        for i in range(2*n):  
            i = i % n
            while stack and nums[stack[-1]] < nums[i]:
                popped_index = stack.pop()                
                result[popped_index] = nums[i]
            
            
            stack.append(i)
        return result
    


s = Solution()
# print(s.nextGreaterElements([1,2,1]))
print(s.nextGreaterElements([1,2,3,5,4,3]))