from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = [0]*n
        res = []
        used = [False]*n

        def get_pernute(A, ans, idx, n, used, res):

            if idx == n:
                cpy = ans[:]
                res.append(cpy)
                return

            for i in range(n):
                if used[i] == False:
                    used[i] = True
                    ans[idx] = A[i]
                    get_pernute(A, ans, idx+1, n, used, res)
                    used[i] = False

        get_pernute(nums, ans, 0, n, used,res)

        return res