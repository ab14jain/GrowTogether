#https://www.geeksforgeeks.org/problems/sum-of-all-substrings-of-a-number-1587115621/1

class Solution:
    def sumSubstrings(self,s):
        # code here

        # Approach 1: Brute Force
        # TC => O(n^3)
        # SC => O(n) for nums creates a temporary substring → takes up to O(n) space at a time.
        # In this approach 
        # 1. Find substring starting with digit at index i and ending every possible j
        # 2. Then convert substring to int and add it to sm variable
        # 3. till doing, you have explored every possible continous numbers
        # For ex = '123'
        # First position = '1', '12','123'
        # Second position = '2', '23'
        # Third position = '3'
        # Sum 1+12+123+2+23+3=164

        # n = len(s)
        # sm = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         nums = s[i:j+1]
        #         sm += int(nums)

        # return sm

        # Approach 2:  To solve the problem follow the below idea:
        # We can solve this problem by using dynamic programming. We can write a summation of all substrings on basis of the digit at which they are ending in that case, 
        # Sum of all substrings = sumofdigit[0] + sumofdigit[1] + sumofdigit[2] … + sumofdigit[n-1] where n is length of string.
        # Where sumofdigit[i] stores the sum of all substring ending at ith index digit, in the above example, 

        # Example: s = "6759"

        # sumofdigit[0] = 6 = 6
        # sumofdigit[1] = 7 + 67  = 74
        # sumofdigit[2] = 5 + 75  + 675 = 755
        # sumofdigit[3] = 9 + 59  + 759 + 6759  = 7586
        # Result = 8421

        # Now we can get the relation between sumofdigit values and can solve the question iteratively. Each sumofdigit can be represented in terms of previous value as shown below, For above example,

        # sumofdigit[3] = 9 + 59  + 759 + 6759 
        #                      =  9 + 50 + 9 + 750 + 9 + 6750 + 9
        #                      = 9*4 + 10*(5 + 75 + 675)
        #                      = 9*4 + 10*(sumofdigit[2])

        # In general, sumofdigit[i]  =  (i+1)*s[i] + 10*sumofdigit[i-1]

        # n = len(s)
        # t_sum = 0
        # prev_sum = 0
        # for i in range(n):
        #     prev_sum = int(s[i])*(i+1)+10*prev_sum

        #     t_sum += prev_sum

        # return t_sum


        #Approach 3: 


        n = len(s)
        total_sum = 0
        mf = 1
        for i in range(n-1, -1, -1):
            total_sum += int(s[i])*(i+1)*mf

            mf = 10*mf+1

        return total_sum

    
s=Solution()
print(s.sumSubstrings("6759"))
print(s.sumSubstrings("675979821"))
print(s.sumSubstrings("421"))
print(s.sumSubstrings("421642456"))
print(s.sumSubstrings("421642456"))