class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        n = len(nums)
        swapped = True
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if nums[j] <= nums[j+1]:
                    continue
                else:
                    # bit count for both number                    
                    prev_num_bits = bin(nums[j]).count('1')
                    next_num_bits = bin(nums[j+1]).count('1')

                    if prev_num_bits == next_num_bits:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        swapped = True
                    else:
                        return False
        
            #no swap happened -- already sorted
            if swapped == 0:
                break    


        return True

s= Solution()
print(s.canSortArray([5,2,6,2])) # False
print(s.canSortArray([2,3,1])) # True
print(s.canSortArray([1,3,2])) # False
print(s.canSortArray([1,2,3])) # True
print(s.canSortArray([1,2,4,8])) # True
print(s.canSortArray([1,2,4,8,16])) # False
        