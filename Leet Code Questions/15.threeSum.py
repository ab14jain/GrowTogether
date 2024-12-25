class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        n = len(nums)
        result = []

        #Brute force approach
        for i in range(n):
            temp = []
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort() # to remove duplicates
                        if temp not in result:                            
                            result.append(temp)

        
        #Approach 2
        for i in range(n):
            temp = []
            for j in range(i+1, n):
                
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort() # to remove duplicates
                        if temp not in result:                            
                            result.append(temp)
        
        return result
    
# Time complexity: O(n^3)
# Space complexity: O(n)
# Time limit exceeded

s=Solution()

print(s.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
print(s.threeSum([0,1,1])) # []
print(s.threeSum([0,0,0])) # [[0,0,0]]             
