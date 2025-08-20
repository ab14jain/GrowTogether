from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        i = 0
        j = 0
        n = len(nums)
        count = 0
        while i<n:
            
            if nums[i] != 0:
                i += 1
            else:
                j = i
                while j < n:
                    if nums[j] == 0:
                        j += 1
                    else:
                        break

                zeros = j-i

                count += (zeros*(zeros+1))//2
                i = j+1
        
        return count
    
s=Solution()
print(s.zeroFilledSubarray([1,3,0,0,2,0,0,4]))
print(s.zeroFilledSubarray([0,0,0,2,0,0]))
print(s.zeroFilledSubarray([2,10,2019]))