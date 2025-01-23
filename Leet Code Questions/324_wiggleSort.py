class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums.sort()
        n = len(nums)
        i = 1
        j = n-1

        res = [0]*n
        while i < n:
            res[i] = nums[j]
            i += 2
            j -= 1

        i = 0
        while j > -1:
            res[i] = nums[j]
            i += 2
            j -= 1       
        
        for i in range(n):
            nums[i] = res[i]
        
        return nums


        

s=Solution()
print(s.wiggleSort([1,5,1,1,6,4])) # [3,5,1,6,2,4]