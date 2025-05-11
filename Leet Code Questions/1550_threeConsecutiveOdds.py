from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        # l = 0
        # r = 0
        # n = len(arr)
        # while r < n-3:
        #     while arr[r] % 2 == 1:
        #         r += 1
        #     if r-l == 3:
        #         return True
        #     r += 1
        #     l = r
        
        # return False

        n = len(arr)
        for i in range(n-2):

            sub_arr = arr[i:i+3]
            has_odd = True
            for num in sub_arr:
                if num % 2 == 0:
                    has_odd = False
                    break
            
            if has_odd:
                return True
        
        return False


s=Solution()
print(s.threeConsecutiveOdds([1,1,1]))
print(s.threeConsecutiveOdds([2,6,4,1]))
print(s.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))