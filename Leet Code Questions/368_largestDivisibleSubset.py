from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        nums.sort()
        dp = [1]*n
        prev_idx = [-1]*n
        max_L = 1
        last_chosen_id = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        prev_idx[i] = j

                    if dp[i] > max_L:
                        max_L = dp[i]
                        last_chosen_id = i

        result = []

        while last_chosen_id != -1:
            result.append(nums[last_chosen_id])
            last_chosen_id = prev_idx[last_chosen_id]

        return result





        #=======Start==== TLE 44 / 49 testcases passed=======
        # nums.sort()
        # n = len(nums)
        # ans = []
        
        # def solve(i, arr, prev):

        #     if i >= n:
        #         nonlocal ans
        #         if len(ans) < len(arr):
        #             ans = arr[:]                
        #         return            
            
        #     if prev == -1 or nums[i] % prev == 0:
        #         arr.append(nums[i])
        #         take = solve(i+1, arr, nums[i])
        #         arr.pop()

        #     not_take = solve(i+1, arr, prev)       
            

        # solve(0, [], -1)
        
        # return ans
        #===============End=========================

        # subsets = []
        # n = len(nums)
        # final_ans = []

        # def subset(i, arr:list):

        #     if i == n:
        #         cpy = arr[:]
        #         subsets.append(cpy)
        #         return
            
        #     arr.append(nums[i])

        #     sub = arr
        #     m = len(sub)  
                     
        #     for j in range(m):
        #         for k in range(j+1, m):
        #             if (sub[j]%sub[k] == 0 or sub[k]%sub[j] == 0):

        #                 nonlocal final_ans
        #                 if len(final_ans) < len(sub):
        #                     final_ans = sub                            
        #                 inc = subset(i+1, arr)
        #                 arr.pop()

        #                 # nonlocal ans
        #                 # ans.append(sub)
                        

        #     exc = subset(i+1, arr)

        # subset(0, [])
        
        
        # # for i in range(len(subsets)):
        # #     sub = subsets[i]
        # #     m = len(sub)  
        # #     hasAllPairDivisiible = True          
        # #     for j in range(m):
        # #         for k in range(j+1, m):
        # #             if not (sub[j]%sub[k] == 0 or sub[k]%sub[j] == 0):     
        # #                 hasAllPairDivisiible = False                   
        # #                 break
            
        # #     if hasAllPairDivisiible:        
        # #         ans.append(sub)

        # #         if len(final_ans) < len(sub):
        # #             final_ans = sub

        # return final_ans



s=Solution()
print(s.largestDivisibleSubset([1,2,3]))
print(s.largestDivisibleSubset([1,2,4,8]))