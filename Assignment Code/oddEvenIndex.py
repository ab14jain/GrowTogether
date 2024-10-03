class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        n = len(A)
        if (n == 1):
            return 1    
        
        if (n == 2):
            return 0
    
        even_sum = 0
        odd_sum = 0
        
        for i in range(n):
            if (i % 2 == 0):
                even_sum += A[i]
            else:
                odd_sum += A[i]
        
       
        curr_odd = 0
        curr_even = A[0]
        res = 0       
        new_even_sum = 0
        new_odd_sum = 0
    
        
        for i in range(1, n - 1):    
            if (i % 2):
                curr_odd += A[i]
                new_even_sum = (curr_even + odd_sum - curr_odd)
                new_odd_sum = (curr_odd + even_sum - curr_even - A[i])  
            else:
                curr_even += A[i]
                new_odd_sum = (curr_odd + even_sum - curr_even)
                new_even_sum = (curr_even + odd_sum - curr_odd - A[i])

            if (new_even_sum == new_odd_sum):
                res += 1
    
        if (odd_sum == even_sum - A[0]):
            res += 1
    
        if (n % 2 == 1):
            if (odd_sum == even_sum - A[n - 1]):
                res += 1
        else:
            if (even_sum == odd_sum - A[n - 1]):  
                res += 1
    
        return res
            

        # Below time complexity is O(n^2) and space complexity is O(1) start
        # count = 0
        # for i in range(0 , len(A)):
        #     even_sum = 0
        #     odd_sum = 0
        #     for j in range(0 , len(A)):
        #         if i != j:
        #             if i > j:
        #                 if (j - 1) % 2 == 0:
        #                     even_sum += A[j]
        #                 else:
        #                     odd_sum += A[j]
        #             else:
        #                 if j % 2 == 0:
        #                     even_sum += A[j]
        #                 else:
        #                     odd_sum += A[j]
        #     if even_sum == odd_sum:
        #         count += 1
        #     #print(f"i: {i}, even_sum: {even_sum}, odd_sum: {odd_sum}")
        
        # return count
        # Below time complexity is O(n^2) and space complexity is O(1) end


sol = Solution()

A = [2, 1, 6, 4]
#A = [1,1,1]
print(sol.solve(A)) # [1]
                        