from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        bin_arr = []
        n = len(nums[0])


        def backtracking(bin_str):

            if len(bin_str) == n:
                bin_arr.append(bin_str)
                return 

            backtracking(bin_str+'1')
            backtracking(bin_str+'0')
            # withone = backtracking(bin_str+'1')
            # withzero = backtracking(bin_str+'0')
            # if withone:
            #     bin_arr.append(withone)
            
            # if withzero:
            #     bin_arr.append(withzero)

        
        backtracking("1")
        backtracking("0")

        for num in bin_arr:

            if num not in nums:
                return num


s=Solution()
print(s.findDifferentBinaryString(["1"]))
print(s.findDifferentBinaryString(["10", "01"]))
print(s.findDifferentBinaryString(["111", "011","001"]))
print(s.findDifferentBinaryString(["1111", "0101","0101"]))

        