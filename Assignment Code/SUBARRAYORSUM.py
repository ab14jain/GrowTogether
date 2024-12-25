from math import log2


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # # 1st Approach
        # total_sum = 0
        # n = len(A)
        # # for i in range(n):
        # #     temp_sum = 0
        # #     passt = []
        # #     for j in range(i, n):
        # #         temp_sum = temp_sum | A[j]
        # #         #passt.append(A[j])
        # #         total_sum = total_sum + temp_sum
        # #         #print(passt, temp_sum, total_sum)

        # for i in range(n):
        #     total_sum = total_sum + A[i]*(i+1)*(n-i)

        
        # return total_sum  % (10**9 + 7)

        # 2nd Approach
        or_sum = 0
        n = len(A)
        max_A = max(A)
        max_bit = int(log2(max_A) + 1)
        total_sum = n * (n+1) // 2
        
        for i in range(max_bit):
            unset_bit = []
            for j in range(n) : 
                a = A[j] >> i                
                if (not(a & 1)) :
                    unset_bit.append(j)  

            
            count_subarr_unset = 0 
            count = 1
    
            for j in range(1, len(unset_bit)) :             
                if (unset_bit[j] - unset_bit[j - 1] == 1) : 
                    count += 1             
                else :                 
                    count_subarr_unset += count * (count + 1) // 2 
                    count = 1

            count_subarr_unset += count * (count + 1) // 2
            if len(unset_bit) == 0:
                count_subarr_unset = 0   
            count_subarr_i_set = total_sum - count_subarr_unset 
    
            or_sum += count_subarr_i_set * pow(2, i) 
     
        return or_sum % (10**9 + 7)
    

# Driver code
s = Solution()
print(s.solve([347148,221001,394957,729925,276769,40726,552988,29952,184491,146773,418965,307,219145,183037,178111,81123,109199,683929,422034,346291,11434,7327,340473,316152,364005,359269,170935,105784,224044,22563,48561,165781,9329,357681,169473,175031,605611,374501,6607,329965,76068,836137,103041,486817,195549,107317,34399,56907,37477,189690,36796,376663,39721,177563,174179,183646,217729,408031,429122,631665,282941,526797,262186,306571,63613,57501,70685,226381,1338,9360,130360,20300,400906,87823,180349,108813,18181,119185,1,102611,63591,12889,311185,383896,8701,76077,75481,386017,153553,304913,383455,105948,142885,1,12610,137005,119185,16948,66171,123683])) # 12
# print(s.solve([1, 2, 3])) # 6
# print(s.solve([1, 2, 3, 4, 5])) # 71
# print(s.solve([7, 8, 9, 10])) # 110
# print(s.solve([1, 2, 3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9])) # 1008
