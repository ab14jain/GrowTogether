from collections import Counter, defaultdict
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]: 
        
        ans = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i==j or j==k or k==i:
                        continue

                    if digits[i] != 0 and digits[k]%2==0:
                        ans.add((digits[i],digits[j],digits[k]))
        
        result = []

        for a,b,c in ans:
            digit = str(a)+str(b)+str(c)
            result.append(int(digit))

        result.sort()
        return result
        # h_map = Counter(digits)
        # all_without_zero = []
        # even_arr = []

        # n = len(digits)
        # for i in range(n):
        #     if digits[i] % 2 == 0:
        #         even_arr.append(digits[i])
            
        #     if digits[i] != 0:
        #         all_without_zero.append(digits[i])
        
        # ans = []
        # for i in range(len(all_without_zero)):
        #     temp = [0]*3
        #     temp[0] = all_without_zero[i]
        #     for j in range(n):
        #         if j != i:
        #             temp[1] = digits[j]
        #             for k in range(len(even_arr)):
        #                 temp[2] = even_arr[k]                
        #                 ans.append(temp[:])
        
        # return ans



s=Solution()
print(s.findEvenNumbers([2,1,3,0]))