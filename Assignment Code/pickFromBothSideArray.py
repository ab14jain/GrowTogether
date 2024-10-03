class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        n = len(A)
        prefix_sum = 0
        postfix_sum = 0
        
        for i in range(B):
            prefix_sum += A[i]
            postfix_sum += A[n - i - 1]
        
        new_prefix_sum = 0
        new_postfix_sum = 0
        temp_postfix_sum = postfix_sum
        mix_sum = -100000
        for i in range(B - 1):
            new_prefix_sum += A[i]  
            new_postfix_sum = temp_postfix_sum - A[n - B + i]
            temp_postfix_sum = new_postfix_sum
            mix_sum = max(mix_sum, new_prefix_sum + new_postfix_sum)

        return max(prefix_sum, postfix_sum, mix_sum)

        # time complexity is O(n ^ 2) and space complexity is O(1)
        # n = len(A)
        # prefix_sum = 0
        # postfix_sum = 0
        # mix_sum = 0
        # for i in range(B):
        #     prefix_sum += A[i]
        #     postfix_sum += A[n - i - 1]
        #     temp_sum = 0
        #     for j in range(i+1):
        #         temp_sum += A[j]
            
        #     for k in range(B - i - 1):
        #         temp_sum += A[n - k - 1]
            
        #     mix_sum = max(mix_sum, temp_sum)
        
        # #print(prefix_sum, postfix_sum, mix_sum)
        # return max(prefix_sum, postfix_sum, mix_sum)

sol = Solution()
#print(sol.solve([5, -2, 3 , 1, 2], 3)) # 8
#print(sol.solve([2, 3, -1, 4, 2, 1], 4)) # 9

print(sol.solve([-969,-948,350,150,-59,724,966,430,107,-809,-993,337,457,-713,753,-617,-55,-91,-791,758,-779,-412,-578,-54,506,30,-587,168,-100,-409,-238,655,410,-641,624,-463,548,-517,595,-959,602,-650,-709,-164,374,20,-404,-979,348,199,668,-516,-719,-266,-947,999,-582,938,-100,788,-873,-533,728,-107,-352,-517,807,-579,-690,-383,-187,514,-691,616,-65,451,-400,249,-481,556,-202,-697,-776,8,844,-391,-11,-298,195,-515,93,-657,-477,587], 81)) # 2

#generate random number from negatve to positive 10^5
# import random
# for i in range(10):
#     print(random.randint(-100000, 100000))
#generate random number from 1 to 10^5
