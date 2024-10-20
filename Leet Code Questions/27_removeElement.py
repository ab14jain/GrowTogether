class Solution:
    def removeElement(self, nums: list[int], val: int) -> list[int]:
        n = len(nums)
        if n == 0:
            return 0
                    
        i = 0
        j = n - 1
        
        while i <= j:
            if nums[i] == val and nums[j] == val:
                j -= 1
            elif nums[i] == val:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j -= 1
                i += 1
            else:
                i += 1
            
            if nums[j] == val:
                j -= 1           
        
        print(i)
        return nums
    
s = Solution()

print(s.removeElement([3,2,2,3], 3)) # [None, 2, 2, None]
# print(s.removeElement([0,1,2,2,3,0,4,2], 2)) # [0, 1, None, None, 3, 0, 4, None]
# print(s.removeElement([0,1,2,2,3,0,4,2], 2)) # [0, 1, None, None, 3, 0, 4, None]
# print(s.removeElement([0], 0)) # [None]
# print(s.removeElement([0,0,0,0,0,0,0,0], 0)) # [None, None, None, None, None, None, None, None]
# print(s.removeElement([1,2,3,4,5,6,7,8], 0)) # [1, 2, 3, 4, 5, 6, 7, 8]
# print(s.removeElement([1,2,3,4,5,6,7,8], 1)) # [None, 2, 3, 4, 5, 6, 7, 8]
