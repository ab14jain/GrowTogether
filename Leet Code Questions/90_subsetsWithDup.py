from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        ans = []
        n = len(nums)
        nums.sort()
        def generate(A, ans, idx, n):

            if idx == n:
                cpy = ans[:]
                res.add(tuple(cpy))
                return
            
            ans.append(A[idx])
            include = generate(A, ans, idx+1, n)
            ans.pop()

            exclude = generate(A, ans, idx+1, n)


        generate(nums, ans, 0, n)
        return list(res)