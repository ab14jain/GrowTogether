from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        # res = []
        # ans = []
        # n = len(nums)
        # def generate(ans, idx):
        #     if idx == n:
        #         cpy = ans[:]
        #         res.append(cpy)
        #         return
            
        #     ans.append(nums[idx])
        #     include = generate(ans, idx+1)
        #     ans.pop()

        #     exclude = generate(ans, idx+1)


        # generate(ans, 0)

        # xor_sum = 0

        # for i in range(len(res)):
        #     t_sum = 0

        #     for j in res[i]:
        #         t_sum ^= j
            
        #     xor_sum += t_sum

        # return xor_sum
    
        subset = []
        n = len(nums)
        def recur(i, arr):
            if i == n:                
                cpy = arr[:]
                subset.append(cpy)
                return

            arr.append(nums[i])

            recur(i+1, arr)
            arr.pop()            
            recur(i+1, arr)

        temp  = []
        recur(0, temp)
        print(subset)



        
        # n = len(nums)
        # xor_sum = 0
        # subset = set()
        # for i in range(n):
        #     for j in range(i,n):                
        #         subset.add(tuple(nums[i:j+1]))
            
        #     for j in range(i+1,n):
        #         subset.add(tuple([nums[i], nums[j]]))
                
        
        # for i in subset:
        #     t_sum = 0
        #     for j in i:
        #         t_sum ^= j
            
        #     xor_sum += t_sum
        # return xor_sum

        # n = len(nums)
        # xor_sum = 0

        # def recur(i):

        #     if i >= n:
        #         return
            
        #     x_sum = 0

        #     for j in range(i,n):
        #         x_sum ^= nums[j]
            
        #     return x_sum
            

            


    

s=Solution()
print(s.subsetXORSum([1,3]))
print(s.subsetXORSum([5,1,6]))
print(s.subsetXORSum([3,4,5,6,7,8]))