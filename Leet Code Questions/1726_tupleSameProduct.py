from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        def nC2(n):
            return (n*(n-1))//2
        prod_map = {}
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                prod = nums[i]*nums[j]
                if prod in prod_map:
                    # prod_map[prod].extend([nums[i],nums[j]])
                    prod_map[prod] += 1
                else:
                    # prod_map[prod] = [nums[i],nums[j]]
                    prod_map[prod] = 1

        count = 0

        for i in prod_map:
            count += (8*nC2(prod_map[i]))

        return count



s=Solution()
print(s.tupleSameProduct([2,3,4,6]))
print(s.tupleSameProduct([50,2,25,4,100,1]))

        