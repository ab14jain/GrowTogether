# Do not write code to include libraries, main() function or accept any input from the console.
# Initialization code is already written and hidden from you. Do not write code for it again.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Just write your code below to complete the function. Required input is available to you as the function arguments.
        # Do not print the result or any output. Just return the result via this function.
        
        seen = set()
        pref_sum = 0
        for i in range(len(A)):
            if i == 0:                
                pref_sum = pref_sum + A[i]
                seen.add(pref_sum)
            else:
                pref_sum = pref_sum + A[i]
                if pref_sum == 0:
                    return 1
                
                if pref_sum in seen:
                    return 1
                
                seen.add(pref_sum)
        
        return 0
    
# # You can test the code for correctness with the help of given test cases
s=Solution()
# A = [1, 2, 3, 4, 5]
# print(s.solve(A)) # Output: 0
# A = [1, 2, -2, 4, 5]
# print(s.solve(A)) # Output: 1
# A = [1, 2, 3, 4, 5, -15]
# print(s.solve(A)) # Output: 1
A = [-4,4,-1,1]
print(s.solve(A)) # Output: 1